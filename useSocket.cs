using System;
using System.Text;
using System.Net.Sockets;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            string url = "134.175.84.144";
            int port = 9999; //端口 
            string SendStr = "hellow, c#\n";
            SocketObj cont = new SocketObj();
            cont.Connection(url, port);
            cont.Send(SendStr);
            cont.Dispose();
        }

    }
    class SocketObj
    {
        private NetworkStream ns;
        private bool _alreadyDispose = false;
        #region 构造与释构 

        public void EBSocketObj(string url, int port)
        {
            Connection(url, port);
        }

        protected virtual void Dispose(bool isDisposing)
        {
            if (_alreadyDispose) return;
            if (isDisposing)
            {
                if (ns != null)
                {
                    try
                    {
                        ns.Close();
                    }
                    catch (Exception E) { }
                    ns.Dispose();
                }
            }
            _alreadyDispose = true;
        }
        #endregion
        #region IDisposable 成员 
        public void Dispose()
        {
            Dispose(true);
            GC.SuppressFinalize(this);
        }
        #endregion
        #region 打开端口 
        /// <summary> 
        /// 打开端口 
        /// </summary> 
        /// <param name="url">URL或者:IP地址</param> 
        /// <param name="port"></param> 
        /// <returns></returns> 
        public virtual void Connection(string url, int port)
        {
            if (url == null || url == "") return;
            if (port < 0) return;
            if (port.ToString() == string.Empty) port = 80;
            TcpClient tcp = null;
            try
            {
                tcp = new TcpClient(url, port);
            }
            catch (Exception E)
            {
                throw new Exception("Can't connection:" + url);
            }
            this.ns = tcp.GetStream();
        }
        #endregion
        #region 发送Socket 
        /// <summary> 
        /// 发送Socket 
        /// </summary> 
        /// <param name="ns"></param> 
        /// <param name="message"></param> 
        /// <returns></returns> 
        public virtual bool Send(string message)
        {
            if (ns == null) return false;
            if (message == null || message == "") return false;
            byte[] buf = Encoding.ASCII.GetBytes(message);
            try
            {
                ns.Write(buf, 0, buf.Length);
            }
            catch (Exception E)
            {
                throw new Exception("Send Date Fail!");
            }
            return true;
        }
        #endregion
    }
}
