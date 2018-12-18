using System;
using System.Collections.Generic;

namespace AutoRest.Core.Model {
    public class DAGraph<DataT, NodeT> : Graph<DataT, NodeT>
        where NodeT : DAGNode<DataT, NodeT> {
            /**
             * The root node in the graph.
             * nodeTable contains all the nodes in this graph with this as the root.
             */
            private NodeT _rootNode;

            /**
             * The immediate parent graphs of this graph. A parent graph is the one whose root
             * depends on this graph's root.
             */
            protected List<DAGraph<DataT, NodeT>> _parentDAGs;

            /**
             * To perform topological sort on the graph. During sorting queue contains the nodes
             * which are ready to invoke.u

             */
            protected Queue<string> _queue;

            private class Visitor : IVisitor<DataT, NodeT> {
                DAGraph<DataT, NodeT> dAGraph;
            public Visitor(DAGraph<DataT, NodeT> dAGraph) {
                this.dAGraph = dAGraph;
            }
            public void visitNode(Node<DataT, NodeT> node)
            {
                var nodeCast = (DAGNode<DataT, NodeT>)node;
                if (nodeCast.dependencyKeys().Count == 0)
                {
                    return;
                }

                string dependentKey = node.Key;
                foreach (string dependencyKey in nodeCast.dependencyKeys())
                {
                    this.dAGraph.nodeTable[dependencyKey].addDependent(dependentKey);
                }
            }

            public void visitEdge(string fromKey, string toKey, EdgeType edgeType)
            {
                if (edgeType == EdgeType.BACK)
                {
                    throw new System.InvalidOperationException("Detected circular dependency: " + dAGraph.findPath(fromKey, toKey));
                }
            }
        }

        /**
            * Creates a new DAG.
            *
            * @param rootNode the root node of this DAG
            */
        public DAGraph(NodeT rootNode) {
            this._parentDAGs = new List<DAGraph<DataT, NodeT>>();
            this._rootNode = rootNode;
            this._queue = new Queue<string>();
            this._rootNode.setPreparer(true);
            this.addNode(rootNode);
        }

        /**
            * @return true if this DAG is merged with one or more DAG and hence has parents
            */
        public bool hasParents() { return this._parentDAGs.Count > 0; }

        /**
            * @return the root node of the DAG.
            */
        protected NodeT root() { return this._rootNode; }

        /**
            * Checks whether the given node is the root node of this DAG.
            *
            * @param node the node DAGNode to be checked
            * @return true if the given node is the root node
            */
        public bool isRootNode(NodeT node) { return this._rootNode == node; }

        /**
            * @return true if this DAG is the preparer responsible for preparing
            * the DAG for traversal.
            */
        public bool isPreparer() { return this._rootNode.isPreparer(); }

        /**
        * Gets a node from the graph with the given key.
        * @param key the key of the node
        * @return the node
        */
        public NodeT getNode(string key) { return this.nodeTable[key]; }

        /**
         * Mark root of this DAG as depnending on given DAG's root
         *
         * @param dependencyGraph the dependency DAG
         */
        public void addDependencyGraph(DAGraph<DataT, NodeT> dependencyGraph) {
                this._rootNode.addDependency(dependencyGraph._rootNode.Key);
                SortedDictionary<string, NodeT> sourceNodeTable = dependencyGraph.nodeTable;
                SortedDictionary<string, NodeT> targetNodeTable = this.nodeTable;
                this.merge(sourceNodeTable, targetNodeTable);
                dependencyGraph._parentDAGs.Add(this);
                if (this.hasParents()) {
                    this.bubbleUpNodeTable(this, new LinkedList<string>());
                }
            }

            /**
             * Mark root of the given DAG depends on this DAG's root.
             *
             * @param dependentGraph the dependent DAG
             */
            public void addDependentGraph(DAGraph<DataT, NodeT> dependentGraph) {
                dependentGraph.addDependencyGraph(this);
            }

            /**
             * Prepares this DAG for node enumeration using getNext method, each call to getNext returns next node
             * in the DAG with no dependencies.
             */
            public void prepareForEnumeration() {
                if (this.isPreparer()) {
                    foreach (NodeT node in this.nodeTable.Values) {
                        // Prepare each node for traversal
                        node.initialize();
                        if (!this.isRootNode(node)) {
                            // Mark other sub-DAGs as non-ppreparer
                            node.setPreparer(false);
                        }
                    }
                    initializeDependentKeys();
                    initializeQueue();
                }
            }

            /**
             * Gets next node in the DAG which has no dependency or all of its dependencies are resolved and 
             * ready to be consumed.
             *
             * @return next node or null if all the nodes have been explored or no node is available at this moment.
             */
            public NodeT getNext() {
                if (this._queue.Count == 0)
                {
                    return null;
                }
                string nextItemKey = this._queue.Dequeue();
                if (nextItemKey == null) {
                    return null;
                }
                return this.nodeTable[nextItemKey];
            }

            /**
             * Reports that a node is resolved hence other nodes that depend on it can consume it.
             *
             * @param completed the node ready to be consumed
             */
            public void reportCompletion(NodeT completed) {
                completed.setPreparer(true);
                string dependency = completed.Key;
                foreach (string dependentKey in this.nodeTable[dependency].dependentKeys()) {
                    DAGNode<DataT, NodeT> dependent = this.nodeTable[dependentKey];
                    dependent.onSuccessfulResolution(dependency);
                    if (dependent.hasAllResolved()) {
                        this._queue.Enqueue(dependent.Key);
                    }
                }
            }

            /**
             * Reports that a node has faulted.
             *
             * @param faulted the node that faulted
             * @param exception the reason for the fault
             */
            public void reportError(NodeT faulted, Exception exception) {
                faulted.setPreparer(true);
                string dependency = faulted.Key;
                foreach (string dependentKey in this.nodeTable[dependency].dependentKeys()) {
                    DAGNode<DataT, NodeT> dependent = this.nodeTable[dependentKey];
                    dependent.onFaultedResolution(dependency, exception);
                    if (dependent.hasAllResolved()) {
                        this._queue.Enqueue(dependent.Key);
                    }
                }
            }

            /**
             * Initializes dependents of all nodes.
             *
             * The DAG will be explored in DFS order and all node's depndents will be identified,
             * this prepares the DAG for traversal using getNext method, each call to getNext returns next node
             * in the DAG with no dependencies.
             */
            private void initializeDependentKeys() {

            visit(new Visitor(this));
                
            }

            /**
             * Initializes the queue that tracks the next set of nodes with no dependencies or whose
             * dependencies are resolved.
             */
            private void initializeQueue() {
                this._queue.Clear();
                foreach (KeyValuePair<string, NodeT> entry in this.nodeTable) {
                    if (!entry.Value.hasDependencies()) {
                        this._queue.Enqueue(entry.Key);
                    }
                }
                if (this._queue.Count == 0) {
                    throw new System.InvalidOperationException("Detected circular dependency");
                }
            }

            /**
             * Copies entries in the source map to target map.
             *
             * @param source source map
             * @param target target map
             */
            private void merge(SortedDictionary<string, NodeT> source, SortedDictionary<string, NodeT> target) {
                foreach (KeyValuePair<string, NodeT> entry in source) {
                    string key = entry.Key;
                    if (!target.ContainsKey(key)) {
                        target.Add(key, entry.Value);
                    }
                }
            }

            /**
             * Propogates node table of given DAG to all of its ancestors.
             */
            private void bubbleUpNodeTable(DAGraph<DataT, NodeT> from, LinkedList<string> path) {
                if (path.Contains(from._rootNode.Key))
                {
                    path.AddFirst(from._rootNode.Key); // For better error message
                    throw new InvalidOperationException("Detected circular dependency: " + String.Join(" -> ", path));
                }
                path.AddFirst(from._rootNode.Key);
                foreach (DAGraph<DataT, NodeT> to in from._parentDAGs)
                {
                    this.merge(from.nodeTable, to.nodeTable);
                    this.bubbleUpNodeTable(to, path);
                }
                path.RemoveFirst();
            }
        }
}