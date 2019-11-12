using MazeRunner.Classes.Maze;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static MazeRunner.Classes.Utils.Type;

namespace MazeRunner.Classes.Algorithms
{
    public class AlgorithmFactory
    {
        private static AlgorithmFactory factory = null;
        public static AlgorithmFactory GetFactory()
        {
            if (factory == null)
            {
                factory = new AlgorithmFactory();
                return factory;
            }
            else
            {
                return factory;
            }
        }

        public BaseAlgorithm GetAlgorithm(AlgorithmType type,Grid grid)
        {
            switch (type)
            {
                case AlgorithmType.AStar:
                    return new AStar(grid);
                case AlgorithmType.BreadthFirst:
                case AlgorithmType.Dijkstra:
                case AlgorithmType.DepthFirst:
                default:
                    throw new KeyNotFoundException();
            }
        }
    }
}
