const crypto = require('crypto');

let creds = {
  "authHeader": "TEST",
  "authHeaderKey": "auth_key",
  "secret": "CB88B914CC39F961C6C6B2B48C3EB8DB715BED195D7CCBE50E61DB544059535A",
  "url": "https://smartdost.samsungmarketing.in/EstoreActivationService/MobileActivationDetails.svc"
};

function _encrypt(data) {
  let key = Buffer.from(creds.secret, "hex");
  const cipher = crypto.createCipheriv("aes-256-ecb", key, Buffer.alloc(0));
  let enc = cipher.update(_addSalt(data.toString()), "binary", "base64");
  enc += cipher.final("base64");
  console.log(enc);
  return enc;
}

function _addSalt(imei, saltSize = 4) {
  const salt = crypto.randomBytes(saltSize);
  salt[0] = ((salt[0] & 0xFC) | (saltSize & 0x03));
  salt[1] = ((salt[1] & 0xF3) | (saltSize & 0x0C));
  salt[2] = ((salt[2] & 0xCF) | (saltSize & 0x30));
  salt[3] = ((salt[3] & 0x3F) | (saltSize & 0xC0));
  return Buffer.concat([salt, Buffer.from(imei)]);
}


_encrypt("+918138969738");