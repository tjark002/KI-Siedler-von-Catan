public class PlayerScript : MonoBehaviour
{
    public Camera cameraView;
    public GameObject village;
    public GameObject road;
    public float roadRange;

    public Color color;

    public Vector3 playerView;

    public int brick = 0;
    public int wheat = 0;
    public int stone = 0;
    public int wood = 0;
    public int sheep = 0;

    public Text brickTxt, woodTxt, sheepTxt, stoneTxt, wheatTxt;

    public bool isFirstTurn, isSecondTurn;

    public bool freeBuild;
    public bool freeBuildRoad;

    public List<GameObject> villages;
    public List<GameObject> roads;

    public int longestRoad;
    public int victoryPoints;

    private List<GameObject> roadsModified;

