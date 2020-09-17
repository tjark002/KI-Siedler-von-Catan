public class buildVillage : MonoBehaviour
{
    public PlayerScript player;
    public GameManager gameManager;

    private void OnMouseDown()
    {
            GameObject villageInstance = player.BuildVillage(this.transform.position);

            Village villageScript = villageInstance.GetComponent<Village>();
            PlaceScript placeScript = this.GetComponent<PlaceScript>();

            if (placeScript.resourceTile1 != null)
                villageScript.tiles.Add(placeScript.resourceTile1);
            if (placeScript.resourceTile2 != null)
                villageScript.tiles.Add(placeScript.resourceTile2);
            if (placeScript.resourceTile3 != null)
                villageScript.tiles.Add(placeScript.resourceTile3);

            player.villages.Add(villageInstance);
            gameManager.buildVillage = villageInstance;

    }

}