const AdminBro = require("admin-bro");
const AdminBroExpress = require("@admin-bro/express");
const AdminBroMongoose = require("@admin-bro/mongoose");

import Challenge from "./models/Challenge";
import User from "./models/User";

AdminBro.registerAdapter(AdminBroMongoose);

const adminBro = new AdminBro({
  resources: [Challenge, User],
  rootPath: "/admin",
});

const routerAdminBro = AdminBroExpress.buildRouter(adminBro);

export { adminBro, routerAdminBro };
