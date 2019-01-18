using System.Collections.ObjectModel;

namespace AutoRest.Python.DAG
{
    public interface INode<NodeT> where NodeT : INode<NodeT>
    {
        // A key that uniquely identifies this node in the owner graph.
        string Key { get; }

        /**
         * @return data stored in this node
         */
        NodeT Data { get; }

        /**
         * @return whether this node has children
         */
        bool hasChildren();

        /**
         * @return children (neighbours) of this node
         */
        ReadOnlyCollection<string> children();

        /**
         * @param childKey add a child (neighbour) of this node
         */
        void addChild(string childKey);

        /**
         * @param childKey remove child (neighbour) of this node
         */
        void removeChild(string childKey);

        /**
         * Sets reference to the graph owning this node.
         *
         * @param ownerGraph the owning graph
         */
        void setOwner(IGraph<NodeT> ownerGraph);

        /**
         * @return the owner (container) graph of this node.
         */
        IGraph<NodeT> owner();
    }
}
