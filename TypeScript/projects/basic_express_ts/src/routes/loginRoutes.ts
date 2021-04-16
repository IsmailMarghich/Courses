import { NextFunction, Request, Response, Router } from "express";

interface RequestWithBody extends Request {
  body: { [key: string]: string | undefined };
}

const requireAuth = (req: Request, res: Response, next: NextFunction): void => {
  if (req.session && req.session.loggedIn) {
    next();
    return;
  }

  res.status(403);
  res.send("not permitted");
};

const router = Router();

router.get("/login", (req: Request, res: Response) => {
  res.send(`
    <form method="post">
        <div>
            <label>Email</label>
            <input name="email">
        </div>
        <div>
            <label>Password</label>
            <input name="password" type="password">
        </div>
        <button>Submit</button>
    </form>
    `);
});
router.post("/login", (req: RequestWithBody, res: Response) => {
  const { email, password } = req.body;
  if (
    email &&
    password &&
    email === "admin@admin.com" &&
    password === "admin"
  ) {
    req.session = { loggedIn: true };
    res.redirect("/");
    res.send(email + password);
  } else {
    res.send("Invalid email or password");
  }
});
router.get("/", (req: Request, res: Response) => {
  if (req.session && req.session.loggedIn) {
    res.send(`
    <div>
        <div>You are logged in</div>
        <a href="/logout">Logout</a>
    </div>
    `);
  } else {
    res.send(`
    <div>
        <div>You are not logged in</div>
        <a href="/login">Login</a>
    </div>
    `);
  }
});
router.get("/logout", (req: Request, res: Response) => {
  req.session = undefined;
  res.redirect("/");
});

router.get("/protected", requireAuth, (req: Request, res: Response) => {
  res.send("Welcome to protected route, logged in user");
});
export { router };
