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

        public DepthFirst DepthFirst
        {
            get => default;
            set
            {
            }
        }

        public AStar AStar
        {
            get => default;
            set
            {
            }
        }

        public BreadthFirst BreadthFirst
        {
            get => default;
            set
            {
            }
        }

        public Utils.Type Type
        {
            get => default;
            set
            {
            }
        }

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
                    return new BreadthFirst(grid);
                case AlgorithmType.Dijkstra:
                    return null;
                case AlgorithmType.DepthFirst:
                    return new DepthFirst(grid);
                    
                default:
                    throw new KeyNotFoundException();
            }
        }
    }
}
