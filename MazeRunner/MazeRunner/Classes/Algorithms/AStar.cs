using MazeRunner.Classes.Maze;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static MazeRunner.Classes.Utils.Type;

namespace MazeRunner.Classes.Algorithms
{
    public class AStar:BaseAlgorithm
    {
        private readonly List<Node> openList = new List<Node>();
        private readonly List<Coord> neighbours;
        public AStar(Grid grid):base(grid)
        {
            neighbours = new List<Coord>();
            //每生成一个节点Id+1
            Node first = new Node(Id++, null, Origin, 0, GetH(Origin, Destination));
            openList.Add(first);
        }

        public override SearchSummary Run()
        {
            if(CurrentNode == null)
            {
                if (openList.Count == 0)
                    return GetSearchSummary();
                //按F、H升序排列，获取第一个，即代价最小
                CurrentNode = openList.OrderBy(x => x.F).ThenBy(x => x.H).First();
                //从open表中移除,添加到close表
                openList.Remove(CurrentNode);
                Closed.Add(CurrentNode);
                Grid.SetTile(CurrentNode.Coord, TileType.Closed);

                neighbours.AddRange(GetNeighbours(CurrentNode));
            }
            if (neighbours.Any())
            {
                Grid.SetTile(CurrentNode.Coord, TileType.Current);
                var thisNeighbour = neighbours.First();
                neighbours.Remove(thisNeighbour);
                //找到终点
                if (thisNeighbour.Equals(Destination))
                {
                    Path = new List<Coord> { thisNeighbour };
                    int? parentId = CurrentNode.Id;
                    while (parentId.HasValue)
                    {
                        var nextNode = Closed.First(x => x.Id == parentId);
                        Path.Add(nextNode.Coord);
                        parentId = nextNode.ParentId;
                    }
                    Path.Reverse();
                    return GetSearchSummary();
                }


                //计算相关费用
                int curH = GetH(thisNeighbour, Destination);
                int curWeight = Grid.GetTile(thisNeighbour).Weight;
                int curCost = CurrentNode.G + curWeight + curH;
                
                //是否在open表中
                var openListItem = openList.FirstOrDefault(x => x.Id == GetExistingNode(true, thisNeighbour));
                if (openListItem != null && openListItem.F > curCost)
                {
                    // 存在且费用高，更新
                    openListItem.F = curCost;
                    openListItem.ParentId = CurrentNode.Id;
                }

                // 是否在close表中
                var closedListItem = Closed.FirstOrDefault(x => x.Id == GetExistingNode(false, thisNeighbour));
                if (closedListItem != null && closedListItem.F > curCost)
                {
                    // 存在且费用高，更新
                    closedListItem.F = curCost;
                    closedListItem.ParentId = CurrentNode.Id;
                }

                //两表中都不存在，添加到open表
                if (openListItem != null || closedListItem != null) 
                    return GetSearchSummary();
                openList.Add(new Node(Id++, CurrentNode.Id, thisNeighbour, CurrentNode.G + curWeight, curH));
                Grid.SetTile(thisNeighbour, TileType.Open);
            }
            else
            {
                Grid.SetTile(CurrentNode.Coord, TileType.Closed);
                CurrentNode = null;
                return Run();
            }
            return GetSearchSummary();
        }

        private int? GetExistingNode(bool checkOpenList, Coord coordToCheck)
        {
            return checkOpenList ? 
                openList.FirstOrDefault(x => x.Coord.Equals(coordToCheck))?.Id 
                : 
                Closed.FirstOrDefault(x => x.Coord.Equals(coordToCheck))?.Id;
        }

        protected override SearchSummary GetSearchSummary()
        {
            return new SearchSummary
            {
                Path = Path?.ToArray(),
                PathCost = GetPathCost(),
                Operations=Operations++,
                UnexploredListSize = Grid.GetCountOfType(TileType.Empty),
                OpenListSize = openList.Count,
                Neighbours=neighbours.Count
                
            };

        }

        private int GetH(Coord cur,Coord des)
        {
            return GetManhattenDistance(cur, des);
        }
    }
}
