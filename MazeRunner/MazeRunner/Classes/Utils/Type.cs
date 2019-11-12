using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MazeRunner.Classes.Utils
{
    public class Type
    {
        public enum TileType
        {
            Invalid = -1,
            Empty = 0,
            Solid = 1,
            Start = 3,
            End = 4,
            Path = 5,
            Open = 6,
            Closed = 7,
            Current = 8
        }

        public enum AlgorithmType
        {
            AStar = 0,
            Dijkstra = 1,
            BreadthFirst = 2,
            DepthFirst = 3
        }
    }
}
