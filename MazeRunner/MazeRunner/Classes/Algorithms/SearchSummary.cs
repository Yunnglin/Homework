using MazeRunner.Classes.Maze;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MazeRunner.Classes.Algorithms
{
    public class SearchSummary
    {
        public Coord[] Path { set; get; }
        public int PathCost { set; get; }
        public bool PathFound => Path != null;
    }
}
