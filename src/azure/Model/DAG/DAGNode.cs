using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Threading;

namespace AutoRest.Core.Model {
    /**
     * The type representing node in a DAGraph.
     *
     * @param <DataT> the type of the data stored in the node
     * @param <NodeT> the type of the node
     */
    public class DAGNode<DataT, NodeT> : Node<DataT, NodeT>
        where NodeT : DAGNode<DataT, NodeT> {

            /**
             * Keys of other nodes that depend on this node.
             */
            private List<string> _dependentKeys;

             /**
              * To track the dependency resolution count.
              */
            private int _toBeResolved;

            /**
             * Indicates this node is the preparer or not.
             */
            private Boolean _isPreparer;

             /**
              * Creates a DAG node.
              *
              * @param key unique id of the node
              * @param data data to be stored in the node
              */
            public DAGNode(string key, DataT data) : base(key, data) {
                this._dependentKeys = new List<string>(); 
            }

            /**
             * @return a list of keys of nodes in DAGraph that are depndents on this node
             */

            public ReadOnlyCollection<string> dependentKeys() { return this._dependentKeys.AsReadOnly(); }

            /**
             * Mark the node identified by the given key as a depndent of this node.
             *
             * @param key the id of the dependent node
             */
            public void addDependent(string key) { this._dependentKeys.Add(key); }

            /**
             * @return a list of keys of nodes in DAGraph that this node depends on.
             */
            public ReadOnlyCollection<string> dependencyKeys() { return this.children(); }

            /**
             * Mark the node identified by the given key as this node's dependency.
             *
             * @param dependencyKey the id of the dependency node
             */
            public void addDependency(string dependencyKey) { base.addChild(dependencyKey); }

            /**
             * Remove the dependency node identified by the given key from the dependencies.
             *
             * @param dependencyKey the id of the dependency node
             */
            public void removeDependency(string dependencyKey) { base.removeChild(dependencyKey); }

            /**
             * @return true if this node has any dependency
             */
            public Boolean hasDependencies() { return this.hasChildren(); }

            /**
             * Mark or un-mark this node as preparer.
             *
             * @param isPreparer true if this node needs to be marked as preparer, false otherwise.
             */
            public void setPreparer(Boolean isPreparer) { this._isPreparer = isPreparer; }

            /**
             * @return true if this node is marked as preparer
             */
            public Boolean isPreparer() { return this._isPreparer; }

            /**
             * Initialize the node so that traversal can be performed on the parent DAG.
             */
            public void initialize() {
                this._toBeResolved = this._dependentKeys.Count;
                this._dependentKeys.Clear();
            }

            /**
             * @return true if all dependencies of this node are resolved
             */
            Boolean hasAllResolved() { return this._toBeResolved == 0; }

            /**
             * Reports a dependency of this node has been successfully resolved.
             *
             * @param dependencyKey the id of the dependency node
             */
            protected void onSuccessfulResolution(string dependencyKey) {
                if (this._toBeResolved == 0) {
                    throw new SystemException("invalid state - " + this.Key + ": The dependency '" + dependencyKey + "' is already reported or there is no such dependencyKey");
                }
                this._toBeResolved--;
            }

            /**
             * Reports a dependency of this node has been faulted.
             *
             * @param dependencyKey the id of the dependency node
             * @param exception the reason for unsuccessful resolution
             */
            protected void onFaultedResolution(string dependencyKey, Exception exception) {
                if (this._toBeResolved == 0) {
                    throw new SystemException("invalid state - " + this.Key + ": The dependency '" + dependencyKey + "' is already reported or there is no such dependencyKey");
                }
                this._toBeResolved--;
            }
    }
}