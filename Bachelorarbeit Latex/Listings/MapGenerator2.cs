void CreateMap(List<Material> resources, List<Material> numbers, List<GameObject> tiles, List<int> positions, List<GameObject> hexTiles, List<int> ints)
    {
        // Alle Einzelteile des Spielfelds werden durchlaufen
        foreach (GameObject tile in hexTiles) 
        {

            GameObject hexSurface = tile.transform.GetChild(0).gameObject; //Oberflaeche des Sechsecks
            GameObject number = tile.transform.GetChild(1).gameObject; //Nummer auf dem Sechseck

            // Eine zufällige Oberfläche wird dem Sechseck zugewiesen.
            int randomResource = Random.Range(0, resources.Count); 
            hexSurface.GetComponent<Renderer>().sharedMaterial = resources[randomResource]; 

            // Die vergebene Oberfläche kann nicht erneut genutzt werden
            resources.RemoveAt(randomResource);

            // Sofern das Sechseck kein Wüstenfeld ist, erhält es eine Nummer
            if (hexSurface.GetComponent<Renderer>().sharedMaterial != sand)
            {
                number.GetComponent<Renderer>().material = numbers[0];
                tile.GetComponent<Tile>().number = ints[0];
                ints.RemoveAt(0);
                numbers.RemoveAt(0);
            }
            else
            {
                Destroy(number); //Wenn es sich um ein Sandfeld handelt, wird der Nummer-Blueprint gelöscht
            }
        }
    }
}