public class MapGeneratorScript : MonoBehaviour
{

    void Start()
    {

        List<Material> resources = new List<Material>()
        {
            wheat, wheat, wheat, wheat,
            wood, wood, wood, wood,
            sheep, sheep, sheep, sheep,
            brick, brick, brick,
            rock, rock, rock,
            sand
        };

        List<GameObject> hexTiles = new List<GameObject>()
        {
            hex1, hex2, hex3, hex4, hex5, hex6, hex7, hex8, hex9, hex10, hex11, hex12,
            hex13, hex14, hex15, hex16, hex17, hex18, hex19
        };

        List<Material> numbers = new List<Material>()
        {
            num5, num2, num6, num3, num8, num10, num9, num12, num11, num4, num8, num10, num9, num4, num5, num6, num3, num11
        };

        List<int> ints = new List<int>()
        {
            5, 2, 6, 3, 8, 10, 9, 12, 11, 4, 8, 10, 9, 4, 5, 6, 3, 11
        };

        List<int> positions = new List<int>()
        {
            7, 3, 0, 1, 2, 6, 11, 15, 18, 17, 16, 12, 8, 4, 5, 10, 14, 13, 9
        };

        List<GameObject> tiles = new List<GameObject>();

        CreateMap(resources, numbers, tiles, positions, hexTiles, ints);
    }	