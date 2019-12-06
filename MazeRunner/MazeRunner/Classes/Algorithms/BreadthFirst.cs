using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MazeRunner.Classes.Maze;

namespace MazeRunner.Classes.Algorithms
{
    public class BreadthFirst : BaseAlgorithm
    {
        private readonly Queue<Node> queue = new Queue<Node>();
        private List<Coord> neighbours;
       
        public BreadthFirst(Grid grid) : base(grid)
        {
            Node first = new Node(Id++, null, Origin, 0, 0);
            queue.Enqueue(first);
        }

        public override SearchSummary Run()
        {
            if (queue.Count > 0)
            {
                //获取下一个节点
                CurrentNode = queue.Dequeue();
                
                //访问过
                if (AlreadyVisited(CurrentNode.Coord)) {
                    return GetSearchSummary();
                }
                //没有被访问过,加入close表
                Closed.Add(CurrentNode);
                Grid.SetTile(CurrentNode.Coord, Utils.Type.TileType.Closed);

                //获取邻居
                neighbours = GetNeighbours(CurrentNode).ToList();
                foreach(var neighbour in neighbours)
                {
                    if (AlreadyVisited(neighbour))
                        continue;
                    //未访问过加入open表
                    var neighbourNode = new Node(Id++, CurrentNode.Id, neighbour, 0, 0);
                    queue.Enqueue(neighbourNode);
                    Grid.SetTile(neighbour, Utils.Type.TileType.Open);
                    

                    if (neighbour.Equals(Destination))
                    {
                        //是目标,设置为close
                        Closed.Add(neighbourNode);
                        Path = new List<Coord>();

                        var step = Closed.First(x => x.Coord.Equals(Destination));
                        while (!step.Coord.Equals(Origin))
                        {
                            Path.Add(step.Coord);
                            step = Closed.First(x => x.Id == step.ParentId);
                        }
                        Path.Add(Origin);
                        Path.Reverse();
                        return GetSearchSummary();
                    }
                }
            }
            return GetSearchSummary();
        }

        private bool AlreadyVisited(Coord coord)
        {
            return Closed.Any(x => x.Coord.Equals(coord));
        }

        protected override SearchSummary GetSearchSummary()
        {
            return new SearchSummary
            {
                Path = Path?.ToArray(),
                PathCost = GetPathCost(),
                OpenListSize = queue.Count,
                UnexploredListSize = Grid.GetCountOfType(Utils.Type.TileType.Empty),
                Operations = Operations++,
                Neighbours = neighbours.Count
            };
        }
    }
}
