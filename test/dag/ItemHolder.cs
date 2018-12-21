namespace AutoRest.Core.Model
{
    public class ItemHolder : DAGNode<ItemHolder> {
        public ItemHolder(string taskId, string value) : base(taskId)
        {
            this.Value = value;
        }

        string Value { get; set; }
    }
}