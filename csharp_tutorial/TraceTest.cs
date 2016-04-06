using System;
using TraceFunctions;

public class TraceClient
{
	public static void Main(string[] args)
	{
		Trace.Message("Main Starting");
		if (args.Length == 0)
		{
			Console.WriteLine("No arguments have been passed");
		}
		else
		{
			for (int i = 0; i < args.Length; i++)
			{
				Console.WriteLine("ARg[{0}] is [{1}]", i, args[i]);
			}
		}
		Trace.Message("Main Ending");
	}
}
