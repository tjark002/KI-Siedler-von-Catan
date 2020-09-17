public GameObject BuildVillage(Vector3 position)
{
    if (freeBuild || this.HasResourcesForVillage())
    {
        if (!freeBuild)
        {
            brick--;
            wood--;
            sheep--;
            wheat--;
        }
        GameObject villageInstance = Instantiate(village);
        villageInstance.transform.position = position;
        villageInstance.GetComponent<Renderer>().material.color = color;

        freeBuild = false;
        freeBuildRoad = true;

        UpdateResources();

        victoryPoints++;
        return villageInstance;
    }
    return null;
}

public GameObject BuildRoad(Vector3 position, Quaternion rotation)
{
    if (freeBuildRoad || this.HasResourcesForRoad()) 
    { 

        if (!freeBuildRoad)
        {
            brick--;
            wood--;
        }

        GameObject roadInstance = Instantiate(road);
        roadInstance.transform.position = position;
        roadInstance.transform.rotation = rotation;
        roadInstance.transform.Rotate(-90.0f, 0.0f, 0.0f, Space.Self);
        roadInstance.GetComponent<Renderer>().material.color = color;

        freeBuildRoad = false;

        UpdateResources();

        return roadInstance;
    }
    return null;
}