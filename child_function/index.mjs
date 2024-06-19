export const handler = async (event, context) => {
  console.log("EVENT: \n" + JSON.stringify(event, null, 2));
  const data = {
    logStreamName: context.logStreamName,
    name: "Child function"
  }
  return {
    status: 200,
    body: JSON.stringify(data),
    headers: {
      "Content-type": "application/json"
    }
  }; 
};