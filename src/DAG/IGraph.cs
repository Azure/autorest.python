using System;
using System.Collections.Generic;
using System.Text;

namespace AutoRest.Python.DAG {
    public interface IGraph<NodeT> where NodeT : INode<NodeT>
    {
        // The nodes in the graph.
        SortedDictionary<string, NodeT> nodeTable { get; }

        /**
         * @return all nodes in the graph.
         */
        SortedDictionary<string, NodeT>.ValueCollection getNodes();

        /**
         * Adds a node to this graph.
         *
         * @param node the node
         */
        void addNode(NodeT node);

        /**
        * Perform DFS visit in this graph.
        *
        * The directed graph will be traversed in DFS order and the visitor will be notified as
        * search explores each node and edge.
        *
        * @param visitor the graph visitor
        */
        void visit(IVisitor<NodeT> visitor);

        string findPath(string start, string end);
    }
}
