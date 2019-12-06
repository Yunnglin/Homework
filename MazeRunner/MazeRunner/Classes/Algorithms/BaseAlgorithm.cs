using MazeRunner.Classes.Maze;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static MazeRunner.Classes.Utils.Type;

namespace MazeRunner.Classes.Algorithms
{
    public abstract class BaseAlgorithm
    {
        protected readonly Grid Grid;
        protected readonly List<Node> Closed;
        protected List<Coord> Path;
        protected readonly Coord Origin;
        protected readonly Coord Destination;
        protected int Id;
        protected Node CurrentNode;
        protected int Operations;

        protected BaseAlgorithm(Grid grid) : this()
        {
            Grid = grid;
            Origin = Grid.GetStart().Coord;
            Destination = Grid.GetEnd().Coord;
        }

        protected BaseAlgorithm()
        {
            Closed = new List<Node>();
            Operations = 0;
            Id = 1;
        }

        public MainWindow MainWindow
        {
            get => default;
            set
            {
            }
        }

        //开始运行
        public abstract SearchSummary Run();

        //获取节点周围可行节点
        protected virtual IEnumerable<Coord> GetNeighbours(Node current)
        {
            var neighbours = new List<Tile>
            {
                Grid.GetTile(current.Coord.X - 1, current.Coord.Y),
                Grid.GetTile(current.Coord.X + 1, current.Coord.Y),
                Grid.GetTile(current.Coord.X, current.Coord.Y - 1),
                Grid.GetTile(current.Coord.X, current.Coord.Y + 1)
            };

            return neighbours.Where(x => x.Type != TileType.Invalid && x.Type != TileType.Solid).Select(x => x.Coord).ToArray();
        }
        //获取搜寻结果
        protected abstract SearchSummary GetSearchSummary();
        //获取连点之间的曼哈顿距离
        protected static int GetManhattenDistance(Coord origin, Coord destination)
        {
            return Math.Abs(origin.X - destination.X) + Math.Abs(origin.Y - destination.Y);
        }
        //获取路径的花费
        protected int GetPathCost()
        {
            if (Path == null) return 0;

            var cost = 0;
            foreach (var step in Path)
                cost += Grid.GetTile(step.X, step.Y).Weight;

            return cost;
        }
    }
}
