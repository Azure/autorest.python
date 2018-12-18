        
namespace AutoRest.Core.Model {
        /**
         * The edge types in a graph.
         */
        public enum EdgeType {
            /**
            * An edge (u, v) is a tree edge if v is visited the first time.
            */
            TREE,
            /**
            * An edge (u, v) is a forward edge if v is descendant of u.
            */
            FORWARD,
            /**
            * An edge (u, v) is a back edge if v is ancestor of u.
            */
            BACK,
            /**
            * An edge (u, v) is a cross edge if v is neither ancestor or descendant of u.
            */
            CROSS
        }

}