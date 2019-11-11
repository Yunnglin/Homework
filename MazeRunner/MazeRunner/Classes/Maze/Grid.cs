using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static MazeRunner.Classes.Utils.Type;

namespace MazeRunner.Classes.Maze
{
    public class Grid
    {
        private Tile[,] tiles;
        private int xCount, yCount;


        public Grid(int xCount, int yCount)
        {
            this.xCount = xCount;
            this.yCount = yCount;

            tiles = new Tile[xCount, yCount];
            for (int x = 0; x < xCount; x++)
            {
                for (int y = 0; y < yCount; y++)
                {
                    SetTail(x, y, TileType.Empty);
                }
            }
            SetStartAndEnd();
        }

        public void Shuffle()
        {
            Shuffle((int)DateTime.Now.Ticks);
        }

        public void Shuffle(int seed)
        {
            var rand = new Random(seed);

            foreach (var tile in tiles)
            {

                tile.Type = rand.Next(0, 10) > 5 ? 
                    TileType.Solid : TileType.Empty;

                if (tile.Type != TileType.Empty)
                    continue;

                // If it's empty, randomly give the path a weight
                var weightSpread = rand.Next(0, 10);
                if (weightSpread > 8)
                    tile.Weight = 3;
                else if (weightSpread > 6)
                    tile.Weight = 2;
                else
                    tile.Weight = 1;

            }

            SetStartAndEnd();
        }

        public void SetTail(int x, int y, TileType type)
        {
            tiles[x, y] = new Tile
            {
                Coord = new Coord(x, y),
                Type = type,
                Weight = GetTile(x, y)?.Weight ?? 0
            };
            SetStartAndEnd();
        }

        public void SetTail(Coord coord, TileType type)
        {
            SetTail(coord.X, coord.Y, type);
        }

        public Tile GetTile(int x, int y)
        {
            if (x > tiles.GetLength(0) - 1 || x < 0 || y > tiles.GetLength(1) - 1 || y < 0)
                return new Tile { Coord = new Coord(-1, -1), Type = TileType.Invalid };

            return tiles[x, y];
        }


        private void SetStartAndEnd()
        {
            tiles[0, 0] = new Tile
            {
                Coord = new Coord(0, 0),
                Type = TileType.Start
            };
            tiles[xCount - 1, yCount - 1] = new Tile
            {
                Coord = new Coord(xCount - 1, yCount - 1),
                Type = TileType.End
            };
        }

        public Tile GetStart()
        {
            return tiles[0, 0];
        }

        public Tile GetEnd()
        {
            return tiles[xCount - 1, yCount - 1];
        }

        public int GetCountOfType(TileType type)
        {
            var total = 0;
            foreach (var cell in tiles)
            {
                total += cell.Type == type ? 1 : 0;
            }

            return total;
        }
    }
}
