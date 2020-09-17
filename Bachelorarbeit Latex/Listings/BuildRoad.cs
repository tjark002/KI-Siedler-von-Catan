public class BuildRoad : MonoBehaviour
{
    public PlayerScript player;
    public GameManager gameManager;

    private void OnMouseDown()
    {
        GameObject roadInstance = player.BuildRoad(this.transform.position, this.transform.rotation);

        if (roadInstance != null)
        {
            player.roads.Add(roadInstance);
            player.CalculateRoadLength();
            gameManager.buildRoad = roadInstance;

            Destroy(this.gameObject);
        }
    }
}