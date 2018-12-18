using System;
using System.Collections;
using System.Collections.ObjectModel;
using System.Collections.Generic;

namespace AutoRest.Core.Model {
    public class Node<DataT, NodeT> where NodeT : Node<DataT, NodeT> {
        // The graph that owns this node.
        private Graph<DataT, NodeT> _ownerGraph;

        // The collection of child node keys.
        private List<string> _children;

        public Node(string key, DataT data) {
            this.Key = key;
            this.Data = data;
            this._children = new List<String>();
        }

        // A key that uniquely identifies this node in the owner graph.
         public string Key { get; private set; }

        /**
         * @return data stored in this node
         */
         public DataT Data { get; private set; }

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
        public void setOwner(Graph<DataT, NodeT> ownerGraph) {
            if (this._ownerGraph != null) {
                throw new SystemException("Changing owner graph is not allowed");
            }
            this._ownerGraph = ownerGraph;
        }

        /**
         * @return the owner (container) graph of this node.
         */
        public Graph<DataT, NodeT> owner() {
            if (this._ownerGraph == null) {
                throw new SystemException("Required owner graph is not set");
            }
            return this._ownerGraph;
        }

    }
}