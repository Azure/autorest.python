
using AutoRest.Core.Model;

namespace AutoRest.Python.Azure.Tests
{
    class ItemHolder : DAGNode<string, ItemHolder> {
        public ItemHolder(string taskId, string taskItem) : base(taskId, taskItem) {

        }
    }
}