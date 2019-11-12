using MazeRunner.Classes.Utils;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Forms;
using static MazeRunner.Classes.Utils.Type;
using MessageBox = System.Windows.MessageBox;
using MazeRunner.Classes.Algorithms;

namespace MazeRunner
{
    /// <summary>
    /// MainWindow.xaml 的交互逻辑
    /// </summary>
    public partial class MainWindow : Window
    {
        private MazeDrawer mazeDrawer = null;
        private readonly int MinCount = 10;
        private readonly int MaxCount = 20;
        private readonly System.Timers.Timer timer;
        BaseAlgorithm algorithm;
        public MainWindow()
        {
            InitializeComponent();

            SetItemSource();

            timer = new System.Timers.Timer(5);
            timer.Elapsed += RunNextStep;
        }

        public void InitialMaze()
        {
            int seed = FindWorkableSeed();
            mazeDrawer = new MazeDrawer(mazeImage, (int)xCountBox.SelectedItem, (int)yCountBox.SelectedItem, seed);
            mazeDrawer.Draw();
        }

        //设置下拉框的内容
        private void SetItemSource()
        {
            List<int> countList = new List<int>();
            for (int i = MinCount; i <= MaxCount; i += 2)
            {
                countList.Add(i);
            }
            xCountBox.ItemsSource = countList;
            xCountBox.SelectedIndex = 0;
            yCountBox.ItemsSource = countList;
            yCountBox.SelectedIndex = 0;

            Dictionary<AlgorithmType, string> funcDic = new Dictionary<AlgorithmType, string>
            {
                {AlgorithmType.AStar,"A*" },
                {AlgorithmType.Dijkstra,"Dijkstra"},
                {AlgorithmType.BreadthFirst,"Breadth First" },
                {AlgorithmType.DepthFirst,"Depth First" }
            };
            selectFuncBox.ItemsSource = funcDic;
            selectFuncBox.DisplayMemberPath = "Value";
            selectFuncBox.SelectedValuePath = "Key";
            selectFuncBox.SelectedValue = AlgorithmType.AStar;
        }

        //找到有可行路径的迷宫种子
        private int FindWorkableSeed()
        {
            return 0;
        }

        private void generateMazeBtn_Click(object sender, RoutedEventArgs e)
        {
            InitialMaze();
        }

        private void startRunBtn_Click(object sender, RoutedEventArgs e)
        {
            if (mazeDrawer == null)
            {
                MessageBox.Show("请先生成迷宫");
                return;
            }
            algorithm = AlgorithmFactory.GetFactory().GetAlgorithm((AlgorithmType)selectFuncBox.SelectedValue, mazeDrawer.Grid);
            timer.Start();
        }

        private void RunNextStep(object sender, System.Timers.ElapsedEventArgs e)
        {
            timer.Stop();
            var summary = algorithm.Run();
            if (summary.PathFound)
            {
                DrawPath(summary);
            }
            else
            {
                mazeDrawer.Draw();
                timer.Start();
            }

        }
        private void DrawPath(SearchSummary summary)
        {
            foreach (var step in summary.Path)
            {
                mazeDrawer.Grid.SetTile(step, TileType.Path);
                mazeDrawer.Draw();

                System.Threading.Thread.Sleep(25);
            }
        }
    }
}
