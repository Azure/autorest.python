namespace AutoRest.Core.Model
{
    public class ItemHolder : DAGNode<ItemHolder> {
        public ItemHolder(string taskId, string taskItem) : base(taskId, new ItemHolder("a", "b")) {

        }
    }
}