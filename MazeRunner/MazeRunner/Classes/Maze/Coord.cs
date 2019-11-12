using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MazeRunner.Classes.Maze
{
    /**
     * 网格坐标
     */
    public class Coord
    {
        
        public int X { get; set; }
        public int Y { get; set; }
        public Coord(int x,int y)
        {
            X = x;
            Y = y;
        }

        public override bool Equals(object obj)
        {
            Coord des = (Coord)obj;
            return X == des.X && Y == des.Y;
        }

        public override int GetHashCode()
        {
            var hashCode = 1861411795;
            hashCode = hashCode * -1521134295 + X.GetHashCode();
            hashCode = hashCode * -1521134295 + Y.GetHashCode();
            return hashCode;
        }
    }
}
