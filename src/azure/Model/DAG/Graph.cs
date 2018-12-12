using System;
using System.Collections;
using System.Collections.Generic;

namespace AutoRest.Core.Model {
    public class Graph<DataT, NodeT> where NodeT : Node<DataT, NodeT> {
        // The nodes in the graph.
        protected SortedDictionary<string, NodeT> _nodeTable;

        // To track the already visited node while performing DFS.
        private HashSet<string> _visited;

        // To generate node entry and exit time while performing DFS.
        private int _time;

        // To track the entry time to each node while performing DFS.
        private Dictionary<string, int> _entryTime;

        // To track the exit time from each node while performing DFS.
        private Dictionary<string, int> _exitTime;

        // To track the immediate parent node of each node while perfoming DFS.
        private Dictionary<string, string> _parent;

        // To track already processed node while performing DFS.
        private HashSet<string> _processed;

        /**
         * The edge types in a graph.
         */
        public enum EdgeType {
            /**
            * An edge (u, v) is a tree edge if v is visited the first time.
            */
            TREE,
            /**
            * An edge (u, v) is a forward edge if v is descendant of u.
            */
            FORWARD,
            /**
            * An edge (u, v) is a back edge if v is ancestor of u.
            */
            BACK,
            /**
            * An edge (u, v) is a cross edge if v is neither ancestor or descendant of u.
            */
            CROSS
        }

        /**
        * Represents a visitor to be implemented by the consumer who want to visit the
        * graph's nodes in DFS order by calling visit method.
        *
        * @param <U> the type of the node
        */
        public interface IVisitor<U> where U : Node<DataT, NodeT> {
            /**
             * visit a node.
             *
             * @param node the node to be visited
             */
            void visitNode(U node);

            /**
             * Visit an edge.
             *
             * @param fromKey key of the from node
             * @param toKey key of the to node
             * edgeType the edge type
             */
            void visitEdge(string fromKey, string toKey, EdgeType edgeType);

        }

        /**
         * Creates a directed graph.
         */
        public Graph() {
            this._nodeTable = new SortedDictionary<string, NodeT>();
            this._visited = new HashSet<string>();
            this._time = 0;
            this._entryTime = new Dictionary<string, int>();
            this._exitTime = new Dictionary<string, int>();
            this._parent = new Dictionary<string, string>();
            this._processed = new HashSet<string>();
        }

        /**
         * @return all nodes in the graph.
         */
        public SortedDictionary<string, NodeT>.ValueCollection getNodes() { return this._nodeTable.Values; }

        /**
         * Adds a node to this graph.
         *
         * @param node the node
         */
        public void addNode(NodeT node) {
            node.setOwner(this);
            _nodeTable.Add(node.Key, node);
        }

        /**
        * Perform DFS visit in this graph.
        *
        * The directed graph will be traversed in DFS order and the visitor will be notified as
        * search explores each node and edge.
        *
        * @param visitor the graph visitor
        */
        public void visit(IVisitor<Node<DataT, NodeT>> visitor) {
            foreach (KeyValuePair<string, NodeT> item in _nodeTable) {
                if (!_visited.Contains(item.Key)) {
                    this.dfs(visitor, item.Value);
                }
            }
            this._visited.Clear();
            this._time = 0;
            this._entryTime.Clear();
            this._exitTime.Clear();
            this._parent.Clear();
            this._processed.Clear();
        }

        private void dfs(IVisitor<Node<DataT, NodeT>> visitor, Node<DataT, NodeT> node) {
            visitor.visitNode(node);

            string fromKey = node.Key;
            this._visited.Add(fromKey);
            this._time++;
            this._entryTime.Add(fromKey, _time);
            foreach (string toKey in node.children()) {
                if (!this._visited.Contains(toKey)) {
                    this._parent.Add(toKey, fromKey);
                    visitor.visitEdge(fromKey, toKey, edgeType(fromKey, toKey));
                    this.dfs(visitor, this._nodeTable[toKey]);
                } else {
                    visitor.visitEdge(fromKey, toKey, edgeType(fromKey, toKey));
                }
            }
            this._time++;
            this._exitTime.Add(fromKey, this._time);
            this._processed.Add(fromKey);
        }

        private EdgeType edgeType(string fromKey, string toKey) {
            if (this._parent.ContainsKey(toKey) && this._parent[toKey].Equals(fromKey)) {
                return EdgeType.TREE;
            }

            if (this._visited.Contains(toKey) && !this._processed.Contains(toKey)) {
                return EdgeType.BACK;
            }

            if (this._processed.Contains(toKey) && this._entryTime.ContainsKey(toKey) && this._entryTime.ContainsKey(fromKey)) {
                if (this._entryTime[toKey] > this._entryTime[fromKey]) {
                    return EdgeType.FORWARD;
                }

                if (this._entryTime[toKey] < this._entryTime[fromKey]) {
                    return EdgeType.CROSS;
                }
            }

            throw new System.InvalidOperationException("Internal Error: Unable to locate the edge type {" + fromKey + ", " + toKey + "}");
        }

        /**
         * Find the path.
         *
         * @param start key of first node in the path
         * @param end key of last node in the path
         * @return string containing the nodes keys in the path separated by arrow symbol
         */
        protected string findPath(string start, string end) {
            if (start.Equals(end)) {
                return start;
            } else {
                return findPath(start, this._parent[end]) + " -> " + end;
            }
        }
    }
}