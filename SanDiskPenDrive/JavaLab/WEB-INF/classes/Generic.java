import java.io.*;
import javax.servlet.*;

public class Generic extends GenericServlet {
 public void service(ServletRequest req, ServletResponse res) throws 
IOException, ServletException {
 res.setContentType("text/HTML");
 PrintWriter w = res.getWriter();
 w.print(" <html> <head> Gneric-Servlet</head>");
 w.print(" <body bgcolor ='red' >");
 w.print(" <h1> GENERIC SERVLET</h1>");
 w.print(" <h2><a href = "index.html" >Go Back</a></h2></body></html>");
 }
}
