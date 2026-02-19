#!/bin/sh

replaceAll() {
    export inputString="$1"
    export pattern="$2"
    export replacement="$3"

    echo "$inputString" | awk '{
        gsub(ENVIRON["pattern"], ENVIRON["replacement"])
        print
    }'
}

html=$(echo "PCFkb2N0eXBlIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KICA8aGVhZD4KICAgIDxtZXRhIGNoYXJzZXQ9IlVURi04IiAvPgogICAgPGxpbmsgcmVsPSJpY29uIiB0eXBlPSJpbWFnZS9zdmcreG1sIiBocmVmPSIvdml0ZS5zdmciIC8+CiAgICA8bWV0YSBuYW1lPSJ2aWV3cG9ydCIgY29udGVudD0id2lkdGg9ZGV2aWNlLXdpZHRoLCBpbml0aWFsLXNjYWxlPTEuMCIgLz4KICAgIDx0aXRsZT5WaXRlICsgUmVhY3Q8L3RpdGxlPgogICAgPCEtLSB2aXRlLWVudnMgc2NyaXB0IHBsYWNlaG9sZGVyIHhLc1BtTHMzMHN3S3NkSXNWeCAtLT48c2NyaXB0IHR5cGU9Im1vZHVsZSIgY3Jvc3NvcmlnaW4gc3JjPSIvYXNzZXRzL2luZGV4LURKdVZXbGNqLmpzIj48L3NjcmlwdD4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgY3Jvc3NvcmlnaW4gaHJlZj0iL2Fzc2V0cy9pbmRleC1Eb1AwWHNQaC5jc3MiPgogIDwvaGVhZD4KICA8Ym9keSBjbGFzcz0iZmxleCBtaW4taC1mdWxsIGZsZXgtY29sIGJnLVstLXJvb3QtYmddIj4KICAgIDxkaXYgaWQ9InJvb3QiIGNsYXNzPSJpc29sYXRlIGZsZXggZmxleC1hdXRvIGZsZXgtY29sIGJnLVstLXJvb3QtYmddIj48L2Rpdj4KICA8L2JvZHk+CjwvaHRtbD4K" | base64 -d)

if printenv VITE_API_BASE_URL &> /dev/null; then
    VITE_API_BASE_URL_base64=$(printenv VITE_API_BASE_URL | base64)
else
    VITE_API_BASE_URL_base64="eEFwV2RSclg5OWtQclZnZ0UiIgo="
fi
VITE_API_BASE_URL=${VITE_API_BASE_URL:-$(echo "Cg==" | base64 -d)}
BASE_URL_base64="eEFwV2RSclg5OWtQclZnZ0UiLyIK"
BASE_URL=$(echo "Lwo=" | base64 -d)
MODE_base64="eEFwV2RSclg5OWtQclZnZ0UicHJvZHVjdGlvbiIK"
MODE=$(echo "cHJvZHVjdGlvbgo=" | base64 -d)
DEV_base64="eEFwV2RSclg5OWtQclZnZ0VmYWxzZQo="
DEV=$(echo "ZmFsc2UK" | base64 -d)
PROD_base64="eEFwV2RSclg5OWtQclZnZ0V0cnVlCg=="
PROD=$(echo "dHJ1ZQo=" | base64 -d)
if printenv DD_RUM_APPLICATION_ID &> /dev/null; then
    DD_RUM_APPLICATION_ID_base64=$(printenv DD_RUM_APPLICATION_ID | base64)
else
    DD_RUM_APPLICATION_ID_base64="eEFwV2RSclg5OWtQclZnZ0UiIgo="
fi
DD_RUM_APPLICATION_ID=${DD_RUM_APPLICATION_ID:-$(echo "Cg==" | base64 -d)}
if printenv DD_RUM_CLIENT_TOKEN &> /dev/null; then
    DD_RUM_CLIENT_TOKEN_base64=$(printenv DD_RUM_CLIENT_TOKEN | base64)
else
    DD_RUM_CLIENT_TOKEN_base64="eEFwV2RSclg5OWtQclZnZ0UiIgo="
fi
DD_RUM_CLIENT_TOKEN=${DD_RUM_CLIENT_TOKEN:-$(echo "Cg==" | base64 -d)}
if printenv DD_SITE &> /dev/null; then
    DD_SITE_base64=$(printenv DD_SITE | base64)
else
    DD_SITE_base64="eEFwV2RSclg5OWtQclZnZ0UiIgo="
fi
DD_SITE=${DD_SITE:-$(echo "Cg==" | base64 -d)}
if printenv DD_ENV &> /dev/null; then
    DD_ENV_base64=$(printenv DD_ENV | base64)
else
    DD_ENV_base64="eEFwV2RSclg5OWtQclZnZ0UiIgo="
fi
DD_ENV=${DD_ENV:-$(echo "Cg==" | base64 -d)}
if printenv DD_VERSION &> /dev/null; then
    DD_VERSION_base64=$(printenv DD_VERSION | base64)
else
    DD_VERSION_base64="eEFwV2RSclg5OWtQclZnZ0UiIgo="
fi
DD_VERSION=${DD_VERSION:-$(echo "Cg==" | base64 -d)}
if printenv DD_SERVICE &> /dev/null; then
    DD_SERVICE_base64=$(printenv DD_SERVICE | base64)
else
    DD_SERVICE_base64="eEFwV2RSclg5OWtQclZnZ0UiIgo="
fi
DD_SERVICE=${DD_SERVICE:-$(echo "Cg==" | base64 -d)}

processedHtml="$html"

processedHtml=$(replaceAll "$processedHtml" "%VITE_API_BASE_URL%" "VITE_API_BASE_URLxPsZs9swrPvxYpC")
processedHtml=$(replaceAll "$processedHtml" "%BASE_URL%" "BASE_URLxPsZs9swrPvxYpC")
processedHtml=$(replaceAll "$processedHtml" "%MODE%" "MODExPsZs9swrPvxYpC")
processedHtml=$(replaceAll "$processedHtml" "%DEV%" "DEVxPsZs9swrPvxYpC")
processedHtml=$(replaceAll "$processedHtml" "%PROD%" "PRODxPsZs9swrPvxYpC")
processedHtml=$(replaceAll "$processedHtml" "%DD_RUM_APPLICATION_ID%" "DD_RUM_APPLICATION_IDxPsZs9swrPvxYpC")
processedHtml=$(replaceAll "$processedHtml" "%DD_RUM_CLIENT_TOKEN%" "DD_RUM_CLIENT_TOKENxPsZs9swrPvxYpC")
processedHtml=$(replaceAll "$processedHtml" "%DD_SITE%" "DD_SITExPsZs9swrPvxYpC")
processedHtml=$(replaceAll "$processedHtml" "%DD_ENV%" "DD_ENVxPsZs9swrPvxYpC")
processedHtml=$(replaceAll "$processedHtml" "%DD_VERSION%" "DD_VERSIONxPsZs9swrPvxYpC")
processedHtml=$(replaceAll "$processedHtml" "%DD_SERVICE%" "DD_SERVICExPsZs9swrPvxYpC")

processedHtml=$(replaceAll "$processedHtml" "VITE_API_BASE_URLxPsZs9swrPvxYpC" "$VITE_API_BASE_URL")
processedHtml=$(replaceAll "$processedHtml" "BASE_URLxPsZs9swrPvxYpC" "$BASE_URL")
processedHtml=$(replaceAll "$processedHtml" "MODExPsZs9swrPvxYpC" "$MODE")
processedHtml=$(replaceAll "$processedHtml" "DEVxPsZs9swrPvxYpC" "$DEV")
processedHtml=$(replaceAll "$processedHtml" "PRODxPsZs9swrPvxYpC" "$PROD")
processedHtml=$(replaceAll "$processedHtml" "DD_RUM_APPLICATION_IDxPsZs9swrPvxYpC" "$DD_RUM_APPLICATION_ID")
processedHtml=$(replaceAll "$processedHtml" "DD_RUM_CLIENT_TOKENxPsZs9swrPvxYpC" "$DD_RUM_CLIENT_TOKEN")
processedHtml=$(replaceAll "$processedHtml" "DD_SITExPsZs9swrPvxYpC" "$DD_SITE")
processedHtml=$(replaceAll "$processedHtml" "DD_ENVxPsZs9swrPvxYpC" "$DD_ENV")
processedHtml=$(replaceAll "$processedHtml" "DD_VERSIONxPsZs9swrPvxYpC" "$DD_VERSION")
processedHtml=$(replaceAll "$processedHtml" "DD_SERVICExPsZs9swrPvxYpC" "$DD_SERVICE")

json=""
json="$json{"
json="$json\"VITE_API_BASE_URL\":\`$VITE_API_BASE_URL_base64\`,"
json="$json\"BASE_URL\":\`$BASE_URL_base64\`,"
json="$json\"MODE\":\`$MODE_base64\`,"
json="$json\"DEV\":\`$DEV_base64\`,"
json="$json\"PROD\":\`$PROD_base64\`,"
json="$json\"DD_RUM_APPLICATION_ID\":\`$DD_RUM_APPLICATION_ID_base64\`,"
json="$json\"DD_RUM_CLIENT_TOKEN\":\`$DD_RUM_CLIENT_TOKEN_base64\`,"
json="$json\"DD_SITE\":\`$DD_SITE_base64\`,"
json="$json\"DD_ENV\":\`$DD_ENV_base64\`,"
json="$json\"DD_VERSION\":\`$DD_VERSION_base64\`,"
json="$json\"DD_SERVICE\":\`$DD_SERVICE_base64\`"
json="$json}"

script="
    <script data-script-description=\"Environment variables injected by vite-envs\">
      (function (){
        var envWithValuesInBase64 = $json;
        var env = {};
        Object.keys(envWithValuesInBase64).forEach(function (name) {
          const value = new TextDecoder().decode(
            Uint8Array.from(
              atob(envWithValuesInBase64[name]),
              c => c.charCodeAt(0))
          ).slice(0,-1);
          env[name] = value.startsWith(\"xApWdRrX99kPrVggE\") ? JSON.parse(value.slice(\"xApWdRrX99kPrVggE\".length)) : value;
        });
        window.__VITE_ENVS = env;
      })();
    </script>"

scriptPlaceholder="<!-- vite-envs script placeholder xKsPmLs30swKsdIsVx -->"

processedHtml=$(replaceAll "$processedHtml" "$scriptPlaceholder" "$script")

DIR=$(cd "$(dirname "$0")" && pwd)

echo "$processedHtml" > "$DIR/index.html"

swEnv_script="
const envWithValuesInBase64 = $json;
const env = {};
Object.keys(envWithValuesInBase64).forEach(function (name) {
  const value = new TextDecoder().decode(
    Uint8Array.from(
      atob(envWithValuesInBase64[name]),
      c => c.charCodeAt(0))
  ).slice(0,-1);
  env[name] = value.startsWith(\"xApWdRrX99kPrVggE\") ? JSON.parse(value.slice(\"xApWdRrX99kPrVggE\".length)) : value;
});
self.__VITE_ENVS = env;
"

echo "$swEnv_script" > "$DIR/swEnv.js" || echo "Not enough permissions to write to $DIR/swEnv.js"
