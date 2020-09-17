public bool HasResourcesForVillage()
    {
        if (brick >= 1 && wood >= 1 && sheep >= 1 && wheat >= 1)
            return true;
        return false;
    }

    public bool HasResourcesForRoad()
    {
        if (brick >= 1 && wood >= 1)
            return true;
        return false;
    }