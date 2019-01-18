using System;
using System.Collections.Generic;
using System.Text;

namespace AutoRest.Python.DAG
{
    public interface IDAGraph<NodeT> : IGraph<NodeT>
        where NodeT : IDAGNode<NodeT>
    {
        /**
            * @return true if this DAG is merged with one or more DAG and hence has parents
            */
        bool hasParents();

        /**
            * Checks whether the given node is the root node of this DAG.
            *
            * @param node the node DAGNode to be checked
            * @return true if the given node is the root node
            */
        bool isRootNode(NodeT node);

        /**
            * @return true if this DAG is the preparer responsible for preparing
            * the DAG for traversal.
            */
        bool isPreparer();

        /**
        * Gets a node from the graph with the given key.
        * @param key the key of the node
        * @return the node
        */
        NodeT getNode(string key);

        /**
            * Prepares this DAG for node enumeration using getNext method, each call to getNext returns next node
            * in the DAG with no dependencies.
            */
        void prepareForEnumeration();

        /**
            * Gets next node in the DAG which has no dependency or all of its dependencies are resolved and 
            * ready to be consumed.
            *
            * @return next node or null if all the nodes have been explored or no node is available at this moment.
            */
        NodeT getNext();

        /**
            * Reports that a node is resolved hence other nodes that depend on it can consume it.
            *
            * @param completed the node ready to be consumed
            */
        void reportCompletion(NodeT completed);

        /**
            * Reports that a node has faulted.
            *
            * @param faulted the node that faulted
            * @param exception the reason for the fault
            */
        void reportError(NodeT faulted, Exception exception);
    }
}
