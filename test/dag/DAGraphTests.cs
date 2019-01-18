using System;
using System.Collections.Generic;
using AutoRest.Python.DAG;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace AutoRest.Python.Azure.Tests
{
    [TestClass]
    public class DAGraphTests {
        [TestMethod]
        public void testDAGraphGetNext() {
            /**
             *   |-------->[D]------>[B]-----------[A]
             *   |                   ^              ^
             *   |                   |              |
             *  [F]------->[E]-------|              |
             *   |          |                       |
             *   |          |------->[G]----->[C]----
             *   |
             *   |-------->[H]-------------------->[I]
             */
            List<string> expectedOrder = new List<string>();
            expectedOrder.Add("A"); expectedOrder.Add("I"); // Level 0
            expectedOrder.Add("B"); expectedOrder.Add("C"); expectedOrder.Add("H"); // Level 1
            expectedOrder.Add("D"); expectedOrder.Add("G"); // Level 2
            expectedOrder.Add("E"); // Level 3
            expectedOrder.Add("F"); // Level 4

            ItemHolder nodeA = new ItemHolder("A", "dataA");
            ItemHolder nodeI = new ItemHolder("I", "dataI");

            ItemHolder nodeB = new ItemHolder("B", "dataB");
            nodeB.addDependency(nodeA.Key);

            ItemHolder nodeC = new ItemHolder("C", "dataC");
            nodeC.addDependency(nodeA.Key);

            ItemHolder nodeH = new ItemHolder("H", "dataH");
            nodeH.addDependency(nodeI.Key);

            ItemHolder nodeG = new ItemHolder("G", "dataG");
            nodeG.addDependency(nodeC.Key);

            ItemHolder nodeE = new ItemHolder("E", "dataE");
            nodeE.addDependency(nodeB.Key);
            nodeE.addDependency(nodeG.Key);

            ItemHolder nodeD = new ItemHolder("D", "dataD");
            nodeD.addDependency(nodeB.Key);


            ItemHolder nodeF = new ItemHolder("F", "dataF");
            nodeF.addDependency(nodeD.Key);
            nodeF.addDependency(nodeE.Key);
            nodeF.addDependency(nodeH.Key);

            DAGraph<ItemHolder> dag = new DAGraph<ItemHolder>(nodeF);
            dag.addNode(nodeA);
            dag.addNode(nodeB);
            dag.addNode(nodeC);
            dag.addNode(nodeD);
            dag.addNode(nodeE);
            dag.addNode(nodeG);
            dag.addNode(nodeH);
            dag.addNode(nodeI);
            

            dag.prepareForEnumeration();
            ItemHolder nextNode = dag.getNext();
            int i = 0;
            while (nextNode != null)
            {
                Assert.AreEqual(nextNode.Key, expectedOrder[i]);
                dag.reportCompletion(nextNode);
                nextNode = dag.getNext();
                i++;
            }

            Console.WriteLine("Done with testDAGraphGetNext.");
        }

        [TestMethod]
        public void testGraphDependency()
        {
            /**
             *   |-------->[D]------>[B]---------->[A]
             *   |                   ^              ^
             *   |                   |              |
             *  [F]------->[E]-------|              |
             *   |          |                       |
             *   |          |------->[G]----->[C]----
             *   |
             *   |-------->[H]-------------------->[I]
             */
            List<string> expectedOrder = new List<string>();
            expectedOrder.Add("A"); expectedOrder.Add("I"); // Level 0
            expectedOrder.Add("B"); expectedOrder.Add("C"); expectedOrder.Add("H"); // Level 1
            expectedOrder.Add("D"); expectedOrder.Add("G"); // Level 2
            expectedOrder.Add("E"); // Level 3
            expectedOrder.Add("F"); // Level 4

            DAGraph<ItemHolder> graphA = createGraph("A");
            DAGraph<ItemHolder> graphI = createGraph("I");

            DAGraph<ItemHolder> graphB = createGraph("B");
            graphB.addDependencyGraph(graphA);

            DAGraph<ItemHolder> graphC = createGraph("C");
            graphC.addDependencyGraph(graphA);

            DAGraph<ItemHolder> graphH = createGraph("H");
            graphH.addDependencyGraph(graphI);

            DAGraph<ItemHolder> graphG = createGraph("G");
            graphG.addDependencyGraph(graphC);

            DAGraph<ItemHolder> graphE = createGraph("E");
            graphE.addDependencyGraph(graphB);
            graphE.addDependencyGraph(graphG);

            DAGraph<ItemHolder> graphD = createGraph("D");
            graphD.addDependencyGraph(graphB);

            DAGraph<ItemHolder> graphF = createGraph("F");
            graphF.addDependencyGraph(graphD);
            graphF.addDependencyGraph(graphE);
            graphF.addDependencyGraph(graphH);

            DAGraph<ItemHolder> dag = graphF;
            dag.prepareForEnumeration();

            ItemHolder nextNode = dag.getNext();
            int i = 0;
            while (nextNode != null)
            {
                Assert.AreEqual(nextNode.Key, expectedOrder[i]);
                // Process the node
                dag.reportCompletion(nextNode);
                nextNode = dag.getNext();
                i++;
            }
            Console.WriteLine("Done with testGraphDependency.");
        }

        [TestMethod]
        public void testGraphNodeTableBubblingUp()
        {
            // ----------------------------------------------------
            // Graph-1

            /**
             * [B] -----------> [A]
             *  ^                 ^
             *  |                 |
             *  |                 |
             *                    |
             *  [C]----------------
             */
            DAGraph<ItemHolder> graphA = createGraph("A");
            DAGraph<ItemHolder> graphB = createGraph("B");
            DAGraph<ItemHolder> graphC = createGraph("C");

            graphB.addDependencyGraph(graphA);
            graphC.addDependencyGraph(graphA);
            graphC.addDependencyGraph(graphB);

            DAGraph<ItemHolder> graph1Root = graphC;

            // ----------------------------------------------------
            // Graph-2

            /**
             * [E] ---> [D] ---> G
             *  ^
             *  |
             *  |
             *  [F]
             */
            DAGraph<ItemHolder> graphD = createGraph("D");
            DAGraph<ItemHolder> graphE = createGraph("E");
            DAGraph<ItemHolder> graphF = createGraph("F");
            DAGraph<ItemHolder> graphG = createGraph("G");

            graphE.addDependencyGraph(graphD);
            graphD.addDependencyGraph(graphG);
            graphF.addDependencyGraph(graphE);

            DAGraph<ItemHolder> graph2Root = graphF;

            // ----------------------------------------------------
            // Graph-3
            /**
             * [J] ---> [H] ---> I
             */

            DAGraph<ItemHolder> graphJ = createGraph("J");
            DAGraph<ItemHolder> graphH = createGraph("H");
            DAGraph<ItemHolder> graphI = createGraph("I");

            graphJ.addDependencyGraph(graphH);
            graphH.addDependencyGraph(graphI);

            DAGraph<ItemHolder> graph3Root = graphJ;

            // ----------------------------------------------------
            // Graph-4

            // Combine 3 graphs using their roots
            // graph1Root == graphC
            graph1Root.addDependentGraph(graph3Root); // graph3Root == graphJ
            graph1Root.addDependentGraph(graph2Root); // graph2Root == graphF

            DAGraph<ItemHolder> graph4Root1 = graph2Root;   // graphF
            DAGraph<ItemHolder> graph4Root2 = graph3Root;   // graphJ

            /**
             * [B] -----------> [A]
             *  ^                 ^
             *  |                 |
             *  |                 |
             *                    |
             *  [C]----------------
             *  ^ ^              (graph4Root2)
             *  | |
             *  |  ---------------[J] ---> [H] ---> I
             *  |
             *  |                 [E] ---> [D] ---> G
             *  |                  ^
             *  |                  |
             *  |                  |
             *  |-----------------[F]  (graph4Root1)
             */

            //======================================================
            // Validate nodeTables (graph1Root)

            ItemHolder nodeA_G1 = graph1Root.getNode("A");
            Assert.AreEqual(1, nodeA_G1.owner().nodeTable.Count);
            assertExactMatch(nodeA_G1.owner().nodeTable.Keys, new List<string> { "A" });

            ItemHolder nodeB_G1 = graph1Root.getNode("B");
            Assert.AreEqual(2, nodeB_G1.owner().nodeTable.Count);
            assertExactMatch(nodeB_G1.owner().nodeTable.Keys, new List<string>{ "A", "B" });

            ItemHolder nodeC_G1 = graph1Root.getNode("C");
            Assert.AreEqual(3, nodeC_G1.owner().nodeTable.Count);
            assertExactMatch(nodeC_G1.owner().nodeTable.Keys, new List<string>{ "A", "B", "C" });

            //======================================================
            // Validate nodeTables (graph4Root1)

            ItemHolder nodeA_G41 = graph4Root1.getNode("A");
            Assert.AreEqual(1, nodeA_G41.owner().nodeTable.Count);
            assertExactMatch(nodeA_G41.owner().nodeTable.Keys, new List<string>{ "A" });

            ItemHolder nodeB_G41 = graph4Root1.getNode("B");
            Assert.AreEqual(2, nodeB_G41.owner().nodeTable.Count);
            assertExactMatch(nodeB_G41.owner().nodeTable.Keys, new List<string>{ "A", "B" });

            ItemHolder nodeC_G41 = graph4Root1.getNode("C");
            Assert.AreEqual(3, nodeC_G41.owner().nodeTable.Count);
            assertExactMatch(nodeC_G41.owner().nodeTable.Keys, new List<string>{ "A", "B", "C" });

            ItemHolder nodeG_G41 = graph4Root1.getNode("G");
            Assert.AreEqual(1, nodeG_G41.owner().nodeTable.Count);
            assertExactMatch(nodeG_G41.owner().nodeTable.Keys, new List<string>{ "G" });

            ItemHolder nodeD_G41 = graph4Root1.getNode("D");
            Assert.AreEqual(2, nodeD_G41.owner().nodeTable.Count);
            assertExactMatch(nodeD_G41.owner().nodeTable.Keys, new List<string>{ "D", "G" });

            ItemHolder nodeE_G41 = graph4Root1.getNode("E");
            Assert.AreEqual(3, nodeE_G41.owner().nodeTable.Count);
            assertExactMatch(nodeE_G41.owner().nodeTable.Keys, new List<string>{ "E", "D", "G" });

            ItemHolder nodeF_G41 = graph4Root1.getNode("F");
            Assert.AreEqual(7, nodeF_G41.owner().nodeTable.Count);
            assertExactMatch(nodeF_G41.owner().nodeTable.Keys, new List<string>{ "E", "F", "D", "G", "A", "B", "C" });

            //======================================================
            // Validate nodeTables (graph4Root2)

            ItemHolder nodeA_G42 = graph4Root2.getNode("A");
            Assert.AreEqual(1, nodeA_G42.owner().nodeTable.Count);
            assertExactMatch(nodeA_G42.owner().nodeTable.Keys, new List<string>{ "A" });

            ItemHolder nodeB_G42 = graph4Root2.getNode("B");
            Assert.AreEqual(2, nodeB_G42.owner().nodeTable.Count);
            assertExactMatch(nodeB_G42.owner().nodeTable.Keys, new List<string>{ "A", "B" });

            ItemHolder nodeC_G42 = graph4Root2.getNode("C");
            Assert.AreEqual(3, nodeC_G42.owner().nodeTable.Count);
            assertExactMatch(nodeC_G42.owner().nodeTable.Keys, new List<string>{ "A", "B", "C" });

            ItemHolder nodeI_G42 = graph4Root2.getNode("I");
            Assert.AreEqual(1, nodeI_G42.owner().nodeTable.Count);
            assertExactMatch(nodeI_G42.owner().nodeTable.Keys, new List<string>{ "I" });

            ItemHolder nodeH_G42 = graph4Root2.getNode("H");
            Assert.AreEqual(2, nodeH_G42.owner().nodeTable.Count);
            assertExactMatch(nodeH_G42.owner().nodeTable.Keys, new List<string>{ "I", "H" });

            ItemHolder nodeJ_G42 = graph4Root2.getNode("J");
            Assert.AreEqual(6, nodeJ_G42.owner().nodeTable.Count);
            assertExactMatch(nodeJ_G42.owner().nodeTable.Keys, new List<string>{ "I", "H", "J", "A", "B", "C" });

            // System.out.println(combinedGraphRoot.nodeTable.Keys);

            // ----------------------------------------------------
            // Graph-1

            /**
             * [L] -----------> [K]
             *  ^                 ^
             *  |                 |
             *  |                 |
             *                    |
             *  [M]----------------
             */
            DAGraph<ItemHolder> graphK = createGraph("K");
            DAGraph<ItemHolder> graphL = createGraph("L");
            DAGraph<ItemHolder> graphM = createGraph("M");


            graphL.addDependencyGraph(graphK);
            graphM.addDependencyGraph(graphL);
            graphM.addDependencyGraph(graphK);


            // Add a non-root node in this graph as dependency of a non-root node in the first graph.
            //
            graphA.addDependencyGraph(graphL);

            /**
             *                   |---------> [L] -----------> [K]
             *                   |           ^                 ^
             *                   |           |                 |
             *                   |           |                 |
             *                   |                             |
             *                   |           [M]----------------
             *                   |
             * [B] -----------> [A]
             *  ^                 ^
             *  |                 |
             *  |                 |
             *                    |
             *  [C]----------------
             *  ^ ^
             *  | |
             *  |  ---------------[J] ---> [H] ---> I
             *  |
             *  |                 [E] ---> [D] ---> G
             *  |                  ^
             *  |                  |
             *  |                  |
             *  |-----------------[F]   (graph4Root1)
             */

            //======================================================
            // Validate nodeTables (graph4Root1)

            ItemHolder nodeK_G41 = graph4Root1.getNode("K");
            Assert.AreEqual(1, nodeK_G41.owner().nodeTable.Count);
            assertExactMatch(nodeK_G41.owner().nodeTable.Keys, new List<string>{ "K" });

            ItemHolder nodeL_G41 = graph4Root1.getNode("L");
            Assert.AreEqual(2, nodeL_G41.owner().nodeTable.Count);
            assertExactMatch(nodeL_G41.owner().nodeTable.Keys, new List<string>{ "K", "L" });

            ItemHolder nodeA_G41_updated = graph4Root1.getNode("A");
            Assert.AreEqual(3, nodeA_G41_updated.owner().nodeTable.Count);
            assertExactMatch(nodeA_G41_updated.owner().nodeTable.Keys, new List<string>{ "K", "L", "A" });

            ItemHolder nodeB_G41_updated = graph4Root1.getNode("B");
            Assert.AreEqual(4, nodeB_G41_updated.owner().nodeTable.Count);
            assertExactMatch(nodeB_G41_updated.owner().nodeTable.Keys, new List<string>{ "K", "L", "A", "B" });

            ItemHolder nodeC_G41_updated = graph4Root1.getNode("C");
            Assert.AreEqual(5, nodeC_G41_updated.owner().nodeTable.Count);
            assertExactMatch(nodeC_G41_updated.owner().nodeTable.Keys, new List<string>{ "K", "L", "A", "B", "C" });

            ItemHolder nodeF_G41_updated = graph4Root1.getNode("F");
            Assert.AreEqual(9, nodeF_G41_updated.owner().nodeTable.Count);
            assertExactMatch(nodeF_G41_updated.owner().nodeTable.Keys, new List<string>{ "K", "L", "A", "B", "C", "F", "E", "D", "G" });

            ItemHolder nodeG_G41_noUpdate = graph4Root1.getNode("G");
            Assert.AreEqual(1, nodeG_G41_noUpdate.owner().nodeTable.Count);
            assertExactMatch(nodeG_G41_noUpdate.owner().nodeTable.Keys, new List<string>{ "G" });

            ItemHolder nodeD_G41_noUpdate = graph4Root1.getNode("D");
            Assert.AreEqual(2, nodeD_G41_noUpdate.owner().nodeTable.Count);
            assertExactMatch(nodeD_G41_noUpdate.owner().nodeTable.Keys, new List<string>{ "D", "G" });

            ItemHolder nodeE_G41_noUpdate = graph4Root1.getNode("E");
            Assert.AreEqual(3, nodeE_G41_noUpdate.owner().nodeTable.Count);
            assertExactMatch(nodeE_G41_noUpdate.owner().nodeTable.Keys, new List<string>{ "E", "D", "G" });

            Console.WriteLine("Done with testGraphNodeTableBubblingUp.");
        }

        private DAGraph<ItemHolder> createGraph(string resourceName)
        {
            ItemHolder node = new ItemHolder(resourceName, "data" + resourceName);
            DAGraph<ItemHolder> graph = new DAGraph<ItemHolder>(node);
            return graph;
        }

        private void assertExactMatch(SortedDictionary<string,ItemHolder>.KeyCollection set, List<string> values)
        {
            foreach (string s in set) {
                if (!values.Contains(s))
                {
                    Assert.AreEqual("Content of set " + set + " does not match with provided array " + values, false);
                }
            }
        }
    }
}