
namespace AutoRest.Core.Model {
    /**
    * Represents a visitor to be implemented by the consumer who want to visit the
    * graph's nodes in DFS order by calling visit method.
    *
    * @param <U> the type of the node
    */
    public interface IVisitor<DataT, NodeT> where NodeT :  Node<DataT, NodeT> {
        /**
            * visit a node.
            *
            * @param node the node to be visited
            */
        void visitNode(Node<DataT, NodeT> node);

        /**
            * Visit an edge.
            *
            * @param fromKey key of the from node
            * @param toKey key of the to node
            * edgeType the edge type
            */
        void visitEdge(string fromKey, string toKey, EdgeType edgeType);

    }
}