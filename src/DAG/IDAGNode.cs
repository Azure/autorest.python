using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Text;

namespace AutoRest.Python.DAG
{
    public interface IDAGNode<NodeT> : INode<NodeT>
        where NodeT : IDAGNode<NodeT>
    {


        /**
         * @return a list of keys of nodes in DAGraph that are depndents on this node
         */

        ReadOnlyCollection<string> dependentKeys();

        /**
         * Mark the node identified by the given key as a depndent of this node.
         *
         * @param key the id of the dependent node
         */
        void addDependent(string key);

        /**
         * @return a list of keys of nodes in DAGraph that this node depends on.
         */
        ReadOnlyCollection<string> dependencyKeys();

        /**
         * Mark the node identified by the given key as this node's dependency.
         *
         * @param dependencyKey the id of the dependency node
         */
        void addDependency(string dependencyKey);

        /**
         * Remove the dependency node identified by the given key from the dependencies.
         *
         * @param dependencyKey the id of the dependency node
         */
        void removeDependency(string dependencyKey);

        /**
         * @return true if this node has any dependency
         */
        bool hasDependencies();

        /**
         * Mark or un-mark this node as preparer.
         *
         * @param isPreparer true if this node needs to be marked as preparer, false otherwise.
         */
        void setPreparer(bool isPreparer);

        /**
         * @return true if this node is marked as preparer
         */
        bool isPreparer();

        /**
         * Initialize the node so that traversal can be performed on the parent DAG.
         */
        void initialize();

        /**
         * @return true if all dependencies of this node are resolved
         */
        bool hasAllResolved();

        /**
         * Reports a dependency of this node has been successfully resolved.
         *
         * @param dependencyKey the id of the dependency node
         */
        void onSuccessfulResolution(string dependencyKey);

        /**
         * Reports a dependency of this node has been faulted.
         *
         * @param dependencyKey the id of the dependency node
         * @param exception the reason for unsuccessful resolution
         */
        void onFaultedResolution(string dependencyKey, Exception exception);
    }
}
