    public void CalculateRoadLength()
    {
        if (roads.Count > 0)
        {
            List<int> roadLengths = new List<int>();
            foreach(GameObject road in roads)
            {
                roadsModified = new List<GameObject>(roads);
                roadLengths.Add(FindRoadNeighbors(road));
            }
            longestRoad = roadLengths.Max();
        }
        else
        {
            longestRoad = 0;
        }
    }

    private int FindRoadNeighbors(GameObject road)
    {
        int neighbors = 0;
        List<GameObject> roadsUpdated = new List<GameObject>();

        for (int i = 0; i < this.roadsModified.Count;)
        {
            GameObject r = this.roadsModified[i];

            float distance = (road.transform.position - r.transform.position).magnitude;
            if (distance < roadRange)
            {
                roadsModified.Remove(r);
                roadsUpdated.Add(r);
                neighbors++;
            } 
            else
            {
                i++;
            }
        }
        foreach (GameObject r in roadsUpdated)
        {
            neighbors += FindRoadNeighbors(r);
        }
        return neighbors;
    }