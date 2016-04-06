using System;
using System.Diagnostics;

namespace TraceFunctions
{
	public class Trace
	{
		[Conditional("DEBUG")]
		public static void Message(string traceMassage)
		{
			Console.WriteLine("[TRACE] - " + traceMassage);
		}
	}
}
