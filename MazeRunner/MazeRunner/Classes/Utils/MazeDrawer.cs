using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Controls;
using System.Windows.Forms;
using System.Windows.Media.Imaging;
using MazeRunner.Classes.Maze;
using static MazeRunner.Classes.Utils.Type;
using Grid = MazeRunner.Classes.Maze.Grid;

namespace MazeRunner.Classes.Utils
{
    public class MazeDrawer
    {
        private PictureBox mazeImage;
        public Grid Grid { get; }
        public int Seed { get; }

        private int xCount;
        private int yCount;

        private int tileWidth;
        private int tileHeight;

        public MazeDrawer(PictureBox image, int xCount = 10, int yCount = 10, int seed = 0)
        {
            this.xCount = xCount;
            this.yCount = yCount;
            mazeImage = image;
            Grid = new Grid(xCount, yCount);
            if (seed == 0)
                Grid.Shuffle();
            else
            {
                Seed = seed;
                Grid.Shuffle(Seed);
            }
        }

        public void Draw()
        {
            tileWidth = mazeImage.Width / xCount;
            tileHeight = mazeImage.Height / yCount;
            Bitmap bitmap = new Bitmap(mazeImage.Width, mazeImage.Height);

            using (var g = Graphics.FromImage(bitmap))
            {
                var background = new Rectangle(0, 0, bitmap.Width, bitmap.Height);
                g.FillRectangle(new SolidBrush(Color.White), background);

                for (var x = 0; x < xCount; x++)
                {
                    for (var y = 0; y < yCount; y++)
                    {
                        var cell = Grid.GetTile(x, y);
                        switch (cell.Type)
                        {
                            case TileType.Empty:
                                switch (cell.Weight)
                                {
                                    case 2: g.FillRectangle(Brushes.LightGray, GetRectangle(x, y)); break;
                                    case 3: g.FillRectangle(Brushes.Silver, GetRectangle(x, y)); break;
                                }
                                break;
                            case TileType.Solid:
                                g.FillRectangle(Brushes.Black, GetRectangle(x, y));
                                break;
                            case TileType.Path:
                                g.FillRectangle(Brushes.Purple, GetRectangle(x, y));
                                break;
                            case TileType.Open:
                                g.FillRectangle(Brushes.LightSkyBlue, GetRectangle(x, y));
                                break;
                            case TileType.Closed:
                                g.FillRectangle(Brushes.LightSeaGreen, GetRectangle(x, y));
                                break;
                            case TileType.Current:
                                g.FillRectangle(Brushes.Crimson, GetRectangle(x, y));
                                break;
                            case TileType.Start:
                                g.DrawString("S", GetFont(), Brushes.Red, GetPoint(x, y));
                                break;
                            case TileType.End:
                                g.DrawString("E", GetFont(), Brushes.Blue, GetPoint(x, y));
                                break;
                            default:
                                throw new ArgumentOutOfRangeException("Unknown cell type: " + cell);
                        }

                        g.DrawRectangle(Pens.Gray, GetRectangle(x, y));
                    }
                }
            }

            mazeImage.Image = bitmap;
        }

        private Rectangle GetRectangle(int x, int y)
        {
            return new Rectangle(x * tileWidth, y * tileHeight, tileWidth, tileHeight);
        }

        private PointF GetPoint(int x, int y)
        {
            return new PointF(x * tileWidth, y * tileHeight);
        }

        private Font GetFont()
        {
            return new Font(FontFamily.GenericMonospace, Math.Min(tileWidth, tileHeight) / 1.8f, FontStyle.Bold);
        }

    }

}
