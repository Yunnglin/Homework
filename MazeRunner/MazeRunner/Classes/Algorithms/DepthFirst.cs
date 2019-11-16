using MazeRunner.Classes.Maze;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static MazeRunner.Classes.Utils.Type;

namespace MazeRunner.Classes.Algorithms
{
    public class DepthFirst : BaseAlgorithm
    {
        private readonly Stack<Node> stack = new Stack<Node>();

        public DepthFirst(Grid grid) : base(grid)
        {
            Node first = new Node(Id++, null, Origin, 0, 0);
            stack.Push(first);
        }

        public override SearchSummary Run()
        {
            CurrentNode = stack.Peek();
            // 找到
            if (CurrentNode.Coord.Equals(Destination))
            {
                Path = new List<Coord>();
                foreach (var item in stack)
                    Path.Add(item.Coord);

                Path.Reverse();

                return GetSearchSummary();
            }
            // 获取未访问过的相邻节点
            var neighbours = GetNeighbours(CurrentNode).Where(x => !AlreadyVisited(new Coord(x.X, x.Y))).ToArray();
            if (neighbours.Any())
            {
                foreach (var neighbour in neighbours)
                    Grid.SetTile(neighbour,TileType.Open);

                // 从中获取第一个
                var next = neighbours.First();
                var newNode = new Node(Id++, null, next.X, next.Y, 0, 0);
                stack.Push(newNode);
                Grid.SetTile(newNode.Coord, TileType.Current);
            }
            else
            {
                // 没有未访问相邻节点也未找到路径，退出
                var abandonedCell = stack.Pop();
                Grid.SetTile(abandonedCell.Coord, TileType.Closed);
                Closed.Add(abandonedCell);
            }

            return GetSearchSummary();
        }
        private bool AlreadyVisited(Coord coord)
        {
            return stack.Any(x => x.Coord.Equals(coord)) || Closed.Any(x => x.Coord.Equals(coord));
        }
        protected override SearchSummary GetSearchSummary()
        {
            return new SearchSummary
            {
                Path = Path?.ToArray(),
                PathCost = GetPathCost(),
                OpenListSize = stack.Count,
                Operations = Operations++,
                UnexploredListSize = Grid.GetCountOfType(TileType.Empty),

            };
        }
    }
}
