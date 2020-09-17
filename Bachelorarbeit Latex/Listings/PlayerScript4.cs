public void CollectResources(int number)
{
    foreach (GameObject village in villages)
    {
        foreach (GameObject tile in village.GetComponent<Village>().tiles)
        {
            if (tile.GetComponent<Tile>().number == number)
            {
                Debug.Log(tile.GetComponentInChildren<Renderer>().sharedMaterial.name);
                if (tile.GetComponentInChildren<Renderer>().sharedMaterial.name == "wheat 1")
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
        }
    }
    UpdateResources();
}