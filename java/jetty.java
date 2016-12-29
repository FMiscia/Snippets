/**
 *  
 *  Create a simple web server
 *
 **/

//Start new Server
Server server = new Server(8080);

// Create the ResourceHandler. It is the object that
// will actually handle the request for a given file.
ResourceHandler resource_handler = new ResourceHandler();

// Create the ResourceHandler. It is the object that will actually handle the
// request for a given file.
resource_handler.setDirectoriesListed(true);
resource_handler.setWelcomeFiles(new String[]{"/index.html"});
resource_handler.setResourceBase("./");

// Add the ResourceHandler to the server.
HandlerList handlers = new HandlerList();
handlers.setHandlers(new Handler[]{ resource_handler, new DefaultHandler() });
ry{
        server.start();
}catch(Exception e){
      ApplicationWorkbenchWindowAdvisor.logMessage(e);
}


/**
 *  
 *  Create a server with random port
 *
 **/

Server server = new Server(0);

//get the port
int port = ((ServerConnector)server.getConnectors()[0]).getLocalPort();

