using System;
using System.Collections;
using System.Collections.ObjectModel;
using System.Collections.Generic;

namespace AutoRest.Python.DAG {
    public class Node<NodeT> : INode<NodeT>
        where NodeT : INode<NodeT>{
        // The graph that owns this node.
        private IGraph<NodeT> _ownerGraph;

        // The collection of child node keys.
        private List<string> _children;

        public Node(string key) {
            this.Key = key;
            this._children = new List<String>();
        }

        // A key that uniquely identifies this node in the owner graph.
         public string Key { get; private set; }

        /**
         * @return data stored in this node
         */
         public NodeT Data { get; private set; }

        /**
         * @return whether this node has children
         */
        public bool hasChildren() { return this._children.Count != 0; }

        /**
         * @return children (neighbours) of this node
         */
        public ReadOnlyCollection<string> children() { return this._children.AsReadOnly(); }

        /**
         * @param childKey add a child (neighbour) of this node
         */
        public void addChild(string childKey) { this._children.Add(childKey); }

        /**
         * @param childKey remove child (neighbour) of this node
         */
        public void removeChild(string childKey) { this._children.Remove(childKey); }

        /**
         * Sets reference to the graph owning this node.
         *
         * @param ownerGraph the owning graph
         */
        public void setOwner(IGraph<NodeT> ownerGraph) {
            if (this._ownerGraph != null) {
                throw new SystemException("Changing owner graph is not allowed");
            }
            this._ownerGraph = ownerGraph;
        }

        /**
         * @return the owner (container) graph of this node.
         */
        public IGraph<NodeT> owner() {
            if (this._ownerGraph == null) {
                throw new SystemException("Required owner graph is not set");
            }
            return this._ownerGraph;
        }

    }
}