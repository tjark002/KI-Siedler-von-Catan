public class RoadFocus : MonoBehaviour
{
    public bool hasFocus = false;
    public VillageFocus villageFocus;

    private void OnMouseDown()
    {
        hasFocus = !hasFocus;
        if (hasFocus)
            villageFocus.hasFocus = false;
    }
}