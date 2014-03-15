/**
 * Find Left Boundary of current Window
 */
function FindLeftWindowBoundry()
{
	// In IE window.screenLeft is the window's left boundary
	if (window.screenLeft)
	{
		return window.screenLeft;
	}
	
	// In FireFox and others window.screenX is the window's left boundary
	if (window.screenX)
		return window.screenX;
		
	return 0;
}

window.leftWindowBoundry = FindLeftWindowBoundry;


/**
 * Find Left Boundary of the Screen/Monitor
 */
function FindLeftScreenBoundry()
{
	// Check if the window is off the primary monitor in a positive axis
	// X,Y                  X,Y                    S = Screen, W = Window
	// 0,0  ----------   1280,0  ----------
	//     |          |         |  ---     |
	//     |          |         | | W |    |
	//     |        S |         |  ---   S |
	//      ----------           ----------
	if (window.leftWindowBoundry() > window.screen.width)
	{
		return window.leftWindowBoundry() - (window.leftWindowBoundry() - window.screen.width);
	}
	
	// Check if the window is off the primary monitor in a negative axis
	// X,Y                  X,Y                    S = Screen, W = Window
	// 0,0  ----------  -1280,0  ----------
	//     |          |         |  ---     |
	//     |          |         | | W |    |
	//     |        S |         |  ---   S |
	//      ----------           ----------
	// This only works in FireFox at the moment due to a bug in Internet Explorer opening new windows into a negative axis
	// However, you can move opened windows into a negative axis as a workaround
	if (window.leftWindowBoundry() < 0 && window.leftWindowBoundry() > (window.screen.width * -1))
	{
		return (window.screen.width * -1);
	}
	
	// If neither of the above, the monitor is on the primary monitor whose's screen X should be 0
	return 0;
}

window.leftScreenBoundry = FindLeftScreenBoundry;


/**
 * Opens a popUp window, also works in multiple screen modes.
 */
function popupper(url, opt)
{
	window.open(url, 'windowName', 'resizable=1, scrollbars=1, fullscreen=0, height=200, width=650, screenX=' + window.leftScreenBoundry() + ' , left=' + window.leftScreenBoundry() + ', toolbar=0, menubar=0, status=1');
}