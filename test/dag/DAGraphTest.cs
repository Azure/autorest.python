using System;
using System.Collections.Generic;
using AutoRest.Core.Model;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace AutoRest.Python.Azure.Tests {
    [TestClass]
    public class DAGraphTest {
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
            expectedOrder.Add("A"); expectedOrder.Add("I");
            expectedOrder.Add("B"); expectedOrder.Add("C"); expectedOrder.Add("H");
            expectedOrder.Add("D"); expectedOrder.Add("G");
            expectedOrder.Add("E");
            expectedOrder.Add("F");

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
            while (nextNode != null) {
                Assert.AreEqual(nextNode.Key, expectedOrder[i]);
                dag.reportCompletion(nextNode);
                nextNode = dag.getNext();
                i++;
            }

            Console.WriteLine("Done with test DAGraphNext");
        }

        [TestMethod]
        public void testGraphMerge() {
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
            expectedOrder.Add("A"); expectedOrder.Add("I");
            expectedOrder.Add("B"); expectedOrder.Add("C"); expectedOrder.Add("H");
            expectedOrder.Add("D"); expectedOrder.Add("G");
            expectedOrder.Add("E");
            expectedOrder.Add("F");

            DAGraph<ItemHolder> graphA = createGraph("A");
            DAGraph<ItemHolder> graphI = createGraph("I");

            DAGraph<ItemHolder> graphB = createGraph("B");
            graphA.addDependentGraph(graphB);

            DAGraph<ItemHolder> graphC = createGraph("C");
            graphA.addDependentGraph(graphC);

            DAGraph<ItemHolder> graphH = createGraph("H");
            graphI.addDependentGraph(graphH);

            DAGraph<ItemHolder> graphG = createGraph("G");
            graphC.addDependentGraph(graphG);

            DAGraph<ItemHolder> graphE = createGraph("E");
            graphB.addDependentGraph(graphE);
            graphG.addDependentGraph(graphE);

            DAGraph<ItemHolder> graphD = createGraph("D");
            graphB.addDependentGraph(graphD);

            DAGraph<ItemHolder> graphF = createGraph("F");
            graphD.addDependentGraph(graphF);
            graphE.addDependentGraph(graphF);
            graphH.addDependentGraph(graphF);

            DAGraph<ItemHolder> dag = graphF;
            dag.prepareForEnumeration();

            ItemHolder nextNode = dag.getNext();
            int i = 0;
            while (nextNode != null) {
                Assert.AreEqual(nextNode.Key, expectedOrder[i]);
                // Process the node
                dag.reportCompletion(nextNode);
                nextNode = dag.getNext();
                i++;
            }
            Console.WriteLine("Done with testGraphMerge");
        }

        private DAGraph<ItemHolder> createGraph(string resourceName) {
            ItemHolder node = new ItemHolder(resourceName, "data" + resourceName);
            DAGraph<ItemHolder> graph = new DAGraph<ItemHolder>(node);
            return graph;
        }
    }
}