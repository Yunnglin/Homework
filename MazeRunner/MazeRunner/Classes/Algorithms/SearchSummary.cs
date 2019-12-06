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
        public bool PathPossible => OpenListSize > 0 || PathFound|| Neighbours>0;
        public bool PathFound => Path != null;
        public Coord[] Path { set; get; }
        public int PathCost { set; get; }
        public int OpenListSize { get; set; }
        public int UnexploredListSize { get; set; }
        public int Operations { set; get; }
        public int Neighbours { set; get; }

        public BaseAlgorithm BaseAlgorithm
        {
            get => default;
            set
            {
            }
        }
    }
}
