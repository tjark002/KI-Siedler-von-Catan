private void StartAIProcess()
{
    //String path = "Assets\\HalloWelt.jar";
    Process foo = new Process();
    foo.StartInfo.FileName = @"C:\Users\tjark\Desktop\CBRSystem.jar";
    //foo.StartInfo.FileName = Environment.CurrentDirectory + @"\Assets\HalloWelt.jar";
    foo.StartInfo.Arguments = "" + Constants.PORT;
    foo.Start();
    connection = new Connection();
}