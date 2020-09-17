/*
* Sammeln von Ressourcen fuer eine bestimmte Siedlung
*/
public void CollectResourcesForVillage(GameObject village)
{
    foreach (GameObject tile in village.GetComponent<Village>().tiles)
    {
        if (tile.GetComponentInChildren<Renderer>().sharedMaterial.name == "wheat")
        {
            wheat++;
        }
        else if (tile.GetComponentInChildren<Renderer>().sharedMaterial.name == "sheep")
        {
            sheep++;
        }
        else if (tile.GetComponentInChildren<Renderer>().sharedMaterial.name == "rock")
        {
            stone++;
        }
        else if (tile.GetComponentInChildren<Renderer>().sharedMaterial.name == "brick")
        {
            brick++;
        } 
        else if (tile.GetComponentInChildren<Renderer>().sharedMaterial.name == "wood")
        {
            wood++;
        }
    }
    UpdateResources();
}