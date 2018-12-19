using AutoRest.Core.Model;
namespace AutoRest.Python.Model
{
    public class ItemHolder : DAGNode<CompositeTypePy, ItemHolder>
    {
        public ItemHolder(string taskId, CompositeTypePy taskItem) : base(taskId, taskItem)
        {

        }
    }
}
