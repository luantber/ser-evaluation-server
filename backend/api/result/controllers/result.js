"use strict";
const { parseMultipartData, sanitizeEntity } = require("strapi-utils");

/**
 * Read the documentation (https://strapi.io/documentation/v3.x/concepts/controllers.html#core-controllers)
 * to customize this controller
 */

module.exports = {
  // Create
  async create(ctx) {
    let entity;
    if (ctx.is("multipart")) {
      const { data, files } = parseMultipartData(ctx);
      entity = await strapi.services.result.create(data, { files });
    } else {
      entity = await strapi.services.resullt.create(ctx.request.body);
    }
    return sanitizeEntity(entity, { model: strapi.models.result });
  },
};
