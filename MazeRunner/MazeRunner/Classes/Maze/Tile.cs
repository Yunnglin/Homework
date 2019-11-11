using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static MazeRunner.Classes.Utils.Type;

namespace MazeRunner.Classes.Maze
{
    public class Tile
    {
        public Coord Coord { get; set; }
        public TileType Type { get; set; }
        public int Weight { get; set; }
    }
}
